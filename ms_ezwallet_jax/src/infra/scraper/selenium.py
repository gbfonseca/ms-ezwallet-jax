import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation
from ms_ezwallet_jax.src.main.config.configuration import configuration
from webdriver_manager.chrome import ChromeDriverManager

def load_driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    if configuration['PYTHON_ENV'] != 'development':
        options.binary_location = configuration['GOOGLE_CHROME_PATH']
        
        driver = webdriver.Chrome(
            executable_path=configuration['CHROMEDRIVER_PATH'],
            options=options,
            )
        return driver
    else:
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=options,
            )
        return driver

driver = load_driver()

class ScraperAdapter(Scraper):

    def __init__(self):
        pass


    def get_data(self, url: str):
        driver.get(url)
        element = driver.find_element(
            By.XPATH, "//div[@class='conteudo clearfix']//table")
        html_content = element.get_attribute('outerHTML')

        driver.close()
        return html_content
