import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class WebScraper:
    def __init__(self, base_url):
        self.driver = webdriver.Chrome()
        self.base_url = base_url

    def close(self):
        if self.driver:
            self.driver.quit()

    async def get_winner_and_time(self, session, results_link):
        try:
            async with session.get(self.base_url + results_link) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                winner = soup.find("div", id="shw_winner-1").text
                time = soup.select_one(
                    '#plain_content_details table:nth-of-type(14) tr:nth-of-type(2) td:nth-of-type(3)').text
                return winner, time
        except NoSuchElementException:
            logging.warning("Element 'Итоги' not found. Skipping...")
        except Exception as err:
            logging.error(f"An error occurred while scraping 'Итоги': {err}")
        return None, None
