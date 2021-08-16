class Train:
    def __init__(self, locomotive_number: int, train_type: str, route: str):
        self.__locomotive_number = locomotive_number
        self.__train_type = train_type
        self.__route = route
        self.__train_cars = []

    def add_train_car(self, train_car: object):
        self.__train_cars.append(train_car)

    @property
    def __len__(self):
        return len(self.__train_cars)

    @property
    def train_cars(self):
        return self.__train_cars

    @property
    def locomotive_number(self):
        return self.__locomotive_number

    @property
    def route(self):
        return self.__route

    @property
    def train_type(self):
        return self.__train_type
