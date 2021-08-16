from typing import List


class TrainCar:
    def __init__(
            self, number_car: int, seats_in_car: int, passengers: List[str]
    ):
        self.__seats_in_car = seats_in_car
        self.__passengers = passengers
        self.__number_car = number_car

    # TODO: I suggest to add not a number but some dict for example
    def add_passenger(self, passengers: int):
        # seats in car is int and you will get error here
        if len(self.__seats_in_car) <= len(self.__passengers + passengers):
            self.__passengers.append(passengers)
        else:
            print("no seats you can't put people")

    @property
    def __len__(self):
        return self.__passengers

    @property
    def number_car(self):
        return self.__number_car

    @property
    def passengers(self):
        return self.__passengers

    @property
    def seats_in_car(self):
        return self.__seats_in_car

    def __str__(self):
        return f"[{self.__number_car}]"
