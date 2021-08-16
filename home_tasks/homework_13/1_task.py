class LaptopMacBook:
    def __init__(self):
        self.__display = 13
        self.__keyboard = "english"
        self.__model = "MacBook pro 13"
        self.__hard_disk = 128
        self.__operating_system = "MacOS Catalina"

    def __cleaner(self, value: str):
        return value.partition("__")[2]

    def __str__(self):
        start, content, end = "{\n", "", "}"

        for key, value in self.__dict__.items():
            content += f"\t{self.__cleaner(key)}: {value}\n"

        return f"{self.__class__.__name__} {start}{content}{end}"


if __name__ == "__main__":
    test = LaptopMacBook()
    print(test)
    # Almost works but not correctly. Take a look on my modifications
    # -1 point
