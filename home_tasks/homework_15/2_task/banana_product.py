
from product import GreenProduct


class Banana(GreenProduct):
    def __init__(self):
        super().__init__()
        self.__product_type = "fruit"
        self.__taste = "very very tasty"
        self.__colour = "yellow"
        self.__name = "banane"