# Web Scraping and Data Processing

This Python script demonstrates web scraping of procurement data from a website and processing it into a Pandas DataFrame. The code is designed to fetch information from a specific website and collect data related to procurement tenders.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running the script, you should have the following software and libraries installed:

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [Aiohttp](https://aiohttp.readthedocs.io/en/stable/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/web-scraping-project.git
    ```

2. Install the required Python libraries if not already installed:
    ```bash
   pip install pandas aiohttp beautifulsoup4 selenium
   ```

3. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) and make sure it's in your system's PATH.

4. Run the main script:
    ```bash
    python main.py
    ```

5. Follow the instructions in the console to perform a manual login on the website if needed.


## File Structure

The project's file structure is organized as follows:

- **main.py**: The main script that orchestrates web scraping and data processing.

- **data_processor.py**: Contains the `DataProcessor` class for processing the scraped data. It defines the structure of the resulting Pandas DataFrame.

- **web_scraper.py**: Contains the `WebScraper` class responsible for web scraping using Selenium. It interacts with the website to retrieve specific data.

- **LICENSE**: The license file that specifies the project's licensing terms (MIT License).

## Contributing

If you would like to contribute to this project, you're welcome to do so by following the standard GitHub fork and pull request workflow.

## License

This project is open-source and licensed under the MIT License. You can find the full license details in the [LICENSE](LICENSE) file.
