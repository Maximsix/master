
from product import GreenProduct


class Strawbarry(GreenProduct):
    def __init__(self):
        super().__init__()
        self.__product_type = "berry"
        self.__taste = "it is the most tasty"
        self.__colour = "red"
        self.__name = "strawbarry"