from ms_ezwallet_jax.src.domain.usecases.html_parser import HtmlParser
from bs4 import BeautifulSoup


class BeautifulSoupAdapter(HtmlParser):
    def parse_html(self, html_content: str) -> str:
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find(name="table")
        return str(table)
