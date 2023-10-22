import asyncio
import logging
import warnings
from asyncio import Lock
from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup

from data_processor import DataProcessor
from web_scraper import WebScraper

BASE_URL = 'https://reestr.nadloc.kz'
PAGE_RANGE = range(1, 11)
# CONCURRENT_REQUESTS = 10

logging.basicConfig(level=logging.INFO)
logging.getLogger("urllib3").setLevel(logging.ERROR)
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

manual_login_lock = Lock()
manual_login_completed = asyncio.Event()


async def scrape_and_process(session, page_number, web_scraper):
    await manual_login_completed.wait()

    data = []
    url = f'{BASE_URL}/ru/tender/List?p={page_number}&s=100&flt_by_status=0&flt_by_type=0'

    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            table = soup.find('table', class_='table table-hover table-striped')

            for row in table.find_all('tr')[2:]:
                columns = row.find_all('td')
                row_data = [column.get_text(strip=True) for column in columns]
                winner, time = None, None

                if 'Завершен' in row_data[6]:
                    results_link = row.find('a', href=True, text='Итоги')
                    if results_link and 'foreignprotocol' not in results_link['href']:
                        winner, time = await web_scraper.get_winner_and_time(session, results_link['href'])

                row_data.append(winner)
                row_data.append(time)
                data.append(row_data)
    except Exception as err:
        logging.error(f"An error occurred while scraping page {page_number}: {err}")

    return data


async def manual_login():
    input("Please complete manual login and press Enter to continue...")
    manual_login_completed.set()


async def main():
    web_scraper = WebScraper(BASE_URL)

    asyncio.create_task(manual_login())

    async with aiohttp.ClientSession() as session:
        data_processor = DataProcessor()
        tasks = [scrape_and_process(session, page_number, web_scraper) for page_number in PAGE_RANGE]
        results = await asyncio.gather(*tasks)

        data_to_concat = []
        for result in results:
            data_to_concat.extend(result)

        df = data_processor.process_data(data_to_concat)
        print(df)

    web_scraper.close()


if __name__ == "__main__":
    print(datetime.now())
    asyncio.run(main())
    print(datetime.now())
