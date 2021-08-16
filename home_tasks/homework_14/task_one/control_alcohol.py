
class ControlAlcohol:
    def __init__(self, age):
        self.__age = age
        self.__value = None

    def __get__(self, instance, owner):
        return instance.__dict__[self.__age]

    def __set__(self, instance, value):
        if value >= 18:
            self.__value = f'you can drinks alcohol it is very cool'
            instance.__dict__[self.__age] = self.__value
        else:
            self.__value = (f"you can't drinks because you are young, you need to "
                            f"wait {abs(value - 18)} {f'years' if 18 - value > 1 else f'year'}")
            instance.__dict__[self.__age] = self.__value


