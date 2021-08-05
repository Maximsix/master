from abc import ABC


class Car(ABC):
    def __int__(self):
        self.wheels = 4
        self.engine = True
        self.car_body = True
        self.exhaust_system = True
        self.tank = True

    @staticmethod
    def move_forvard(self):
        print("Moving forward")

    @staticmethod
    def move_back(self):
        print("move back")

    @staticmethod
    def stop(self):
        print("stop")

    @staticmethod
    def turn_right(self):
        print("turn right")

    @staticmethod
    def turn_left(self):
        print("turn left")


    def engine_work(self):
        raise NotImplementedError("not implemented")

    def environmental_impact(self):
        raise NotImplementedError("not implemented")

    def refuel_car(self):
        raise NotImplementedError("not implemented")


class ElectroCar(Car):
    def __init__(self):
        super().__init__()
        self.wheels = 4
        self.engine = "electro"
        self.car_body = "metal"
        self.exhaust_system = False
        self.tank = "battery"

    def __quickly_pick_speed(self):
        print('quickly picks up speed to 100')

    def speed(self):
        self.__quickly_pick_speed()

    def engine_work(self):
        print("engine runs without sound")

    def refuel_car(self):
        print("car charge by electricity")

    def environmental_impact(self):
        print("ecology is not polluted")



class DiselCar(Car):
    def __init__(self):
        super().__init__()
        self.wheels = 4
        self.engine = "disel"
        self.car_body = "metal"
        self.exhaust_system = True
        self.tank = "disel"

    def engine_work(self):
        print("engine runs with loud sound")

    def refuel_car(self):
        print("car is refueled at a disel station")

    def __throw_out_gases(self):
        print('car throws out exhaust gases')

    def __set_eco_mode(self):
        print('switch driving mode to eco mod')

    def environmental_impact(self):
        print("pollutes the environment")


    def _gase(self):
        self.__throw_out_gases()

    def _eco(self):
        self.__set_eco_mode()




class TeslaCar(ElectroCar):
    def __init__(self, model: str, type_car_body: str, battery_capacity: int, weight: int):
        self.model = model
        self.type_car_body = type_car_body
        self.battery_capacity = battery_capacity
        self.weight = weight
        self.autopilot = True

    def fast_driving(self):
        self.speed()

    def __control_car(self):
        print("autopilot controls the car")

class RenoCar(DiselCar):
    def __init__(self, model: str, type_car_body: str, volume_of_tank: int, weight: int, engine_volume: float):
        self.model = model
        self.type_car_body = type_car_body
        self.volume_of_tank = volume_of_tank
        self.weight = weight
        self.engine_volume = engine_volume


    def press_pedal(self):
        self._gase()

    def fuel_economy(self):
        self._eco()



if __name__ == '__main__':
    reno_megan = RenoCar("Reno megan", "universal", 45, 1700, 1.5)
    tesla_model_s = TeslaCar("Tesla model S", 'sedan', 100000, 2223)


# Good but don't use static methods since send in them not active -2 poitns
# I see abstraction and incapsulation in method
#     def __quickly_pick_speed(self):
#         print('quickly picks up speed to 100')
#
#     def speed(self):
#         self.__quickly_pick_speed()
# but it would be nice to see state modification instead of simple print of message -2 points
