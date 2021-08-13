
class LaptopMacBook:
    def __init__(self):
        self.__display = 13
        self.__keyboard = "english"
        self.__model = "MacBook pro 13"
        self.__hard_disk = 128
        self.__operating_system = "MacOS Catalina"


    def __cleaner(self, value):
        return value.partition("__")[2]

    def __str__(self):
        result = ""
        for key, value in self.__dict__.items():
            result += (
                f"\n{self.__class__.__name__}:\n{{\n{self.__cleaner(key)}: {value}\n}}\n"
            )
        return result


if __name__ == '__main__':
    test = LaptopMacBook()
