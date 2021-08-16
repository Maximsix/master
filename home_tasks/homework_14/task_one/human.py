
from control_alcohol import ControlAlcohol


class Human:
    __age = ControlAlcohol("age")

    def __init__(self, name: str, age: int, gender: bool):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def drink_alcohol(self):
        return f"{self.__name}, {self.__age }"
