import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper
from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from ms_ezwallet_jax.src.domain.usecases.data_manipulation import DataManipulation

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


class ScraperAdapter(Scraper):

    def __init__(self, html_parser: HtmlParser, data_manipulation: DataManipulation):
        self.html_parser = html_parser
        self.data_manipulation = data_manipulation

    def get_data(self, url: str):
        driver.get(url)
        element = driver.find_element(
            By.XPATH, "//div[@class='conteudo clearfix']//table")
        html_content = element.get_attribute('outerHTML')
        table = self.html_parser.parseHtml(html_content)
        df = self.data_manipulation.to_dict(str(table))
        driver.close()
        return df
