from abc import ABCMeta, abstractmethod


class Scraper(metaclass=ABCMeta):
    @property
    @abstractmethod
    def get_data(self, url: str): raise NotImplementedError


