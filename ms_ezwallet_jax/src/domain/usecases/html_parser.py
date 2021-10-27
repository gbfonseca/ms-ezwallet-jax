from abc import ABCMeta, abstractmethod


class HtmlParser(metaclass=ABCMeta):
    @property
    @abstractmethod
    def parseHtml(self, html_content: str): raise NotImplementedError
