import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
url = 'https://fundamentus.com.br/resultado.php'

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


def get_actions():
    driver.get(url)
    element = driver.find_element(
        By.XPATH, "//div[@class='conteudo clearfix']//table")
    html_content = element.get_attribute('outerHTML')
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name="table")
    df = pd.read_html(str(table), index_col=0)[0]
    return df.to_dict()


def convert_dict_keys_to_english(data: dict):
    data['price'] = data.pop('Cotação')
    return data


dict_of_actions = convert_dict_keys_to_english(get_actions())
print(dict_of_actions)
driver.quit()
