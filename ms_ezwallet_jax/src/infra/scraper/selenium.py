import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


class ScraperAdapter(Scraper):
    def get_data(self, url: str):
        driver.get(url)
        element = driver.find_element(
            By.XPATH, "//div[@class='conteudo clearfix']//table")
        html_content = element.get_attribute('outerHTML')
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name="table")
        df = pd.read_html(str(table), index_col=0)[0]
        return df.to_dict()
