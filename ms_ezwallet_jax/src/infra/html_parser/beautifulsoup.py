from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from bs4 import BeautifulSoup


class BeautifulSoupAdapter(HtmlParser):
    def parseHtml(self, html_content: str):
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name="table")
        return table
