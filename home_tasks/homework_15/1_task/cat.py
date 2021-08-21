from singolton import singolton


@singleton
class Cat:
    def __init__(self, colour: str, breed: str, name: str, age: int):
        self.__colour = colour
        self.__breed = breed
        self.__name = name
        self.__age = age

    @property
    def colour(self):
        return self.__colour

    @property
    def breed(self):
        return self.__breed

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
