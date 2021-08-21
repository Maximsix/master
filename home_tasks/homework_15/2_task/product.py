
from abc import ABC


class GreenProduct(ABC):
    _name: str = ""

    def __init__(self):
        self.__product_type = None
        self.__taste = None
        self.__colour = None
        self.__name = None

    @property
    def name(self):
        return self.__name

    @property
    def product_type(self):
        return self.__product_type

    @property
    def taste(self):
        return self.__taste

    @property
    def colour(self):
        return self.__colou