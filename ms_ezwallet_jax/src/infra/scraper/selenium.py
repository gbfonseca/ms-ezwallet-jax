# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By

from ms_ezwallet_jax.src.domain.usecases.scraper import Scraper


# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options)


class ScraperAdapter(Scraper):

    def __init__(self):
        pass

    def get_data(self, url: str):
        pass
