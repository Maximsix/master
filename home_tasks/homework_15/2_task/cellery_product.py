
from product import GreenProduct


class Cellery(GreenProduct):
    def __init__(self):
        super().__init__()
        self.__product_type = "plant"
        self.__taste = "is not tasty"
        self.__colour = "green"
        self.__name = "cellery"