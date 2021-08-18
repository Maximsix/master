
from product import GreenProduct
from apple_product import Apple
from banana_product import Banana
from cellery_product import Cellery
from strawbarry_product import Strawbarry


class MarketFactory:
    @staticmethod
    def get_product(product_name: str) -> GreenProduct:
        objects_list1 = [Banana, Apple, Cellery, Strawbarry]
        counter = 0
        for x in objects_list1:
            if product_name == (str(x.__name__)).lower():
                return objects_list1[counter]()
            counter += 1


    # my first variant

    # def get_product(product_name: str) ->GreenProduct:
    #     if product_name == "apple":
    #         return Apple()
    #     elif product_name == "banana":
    #         return Banana()
    #     elif product_name == "cellery":
    #         return Cellery()
    #     elif product_name == "strawbarry":
    #         return Strawbarry()










