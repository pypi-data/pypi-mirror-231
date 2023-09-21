from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class Parser(ABC):
    def __init__(self, page) -> None:
        self.page = BeautifulSoup(page,features="lxml")

    @abstractmethod
    def parse(self):
        pass
