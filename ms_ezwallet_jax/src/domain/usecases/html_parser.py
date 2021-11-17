from abc import ABCMeta, abstractmethod


class HtmlParser(metaclass=ABCMeta):
    @property
    @abstractmethod
    def parse_html(self, html_content: str): raise NotImplementedError
