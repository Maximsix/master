
from product import GreenProduct


class Apple(GreenProduct):
    def __init__(self):
        super().__init__()
        self.__product_type = "fruit"
        self.__taste = "very tasty"
        self.__colour = "green"
        self.__name = "apple"

