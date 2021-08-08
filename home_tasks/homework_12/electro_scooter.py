
from move import Move
from electronic_work import ElectronicWork


class ElectroScooterBolt(Move, ElectronicWork):
    def __init__(self):
        self.__wheels = 2
        self.__electric_motor = False
        self.__brake = False
        self.__start_system = False
        self.__battery = 100
        self.__paid = False

    @property
    def trip_pay(self):
        if self.__paid == False:
            self.__paid = True
            print('you paid the trip, turn on the system and ride')
        else:
            print('trip has already been paid, you can ride further')

    @property
    def put_on_system(self):
        if self.__paid == True:
            print("start system")
            self.__start_system = True
        else:
            print('pay for the trip')

    @property
    def wait(self):
        if self.__start_system == True:
            print("waiting for the trip")
        else:
            self.__start_system = False
            print("the system is off, waiting is not possible")

    @property
    def move(self):
        if self.__start_system == True:
            self.__electric_motor = True
            if self.__electric_motor == True:
                if self.__battery <= 10:
                    print("need to charge the scooter")
                else:
                    print('scooter moving')
                    self.__battery -= 50
                    self.__brake = False
            else:
                print('scooter moving again')
        else:
            if self.__start_system == False and self.__paid == False:
                print('you did not pay for the trip, pay please')
            elif self.__paid == True:
                print("please put on system")

    @staticmethod
    def stop(self):
        if self.__start_system == True:
            print("scooter stop")
            print('recommend you have rest 2 minutes')
        else:
            print('control does not work pay the trip')

    @property
    def complete_trip(self):
        if not self.__start_system:
            print("you haven't started your ride yet")
        else:
            self.__electric_motor = False
            self.__start_system = False
            print("trip finished have a nice day")

    @property
    def scooter_breake(self):
        if self.__start_system == True:
            print("scooter goes slowly")
            self.__brake = True
        else:
            print('control does not work pay the trip')

    @property
    def charge(self):
        if self.__start_system == True:
            if self.__battery <= 10:
                self.__battery += 50
                print(f'the battery is charged at 100 \nbattery reserve is {self.__battery}')
            elif self.__battery + 50 >= 100:
                print('battery is already charged')
        else:
            print("the system is off, you can't see, please put on system")

    @property
    def check_kilometers(self):
        if self.__start_system == True:
            self.__kilometers = int(self.__battery / 10)
            print(f"you can drive more {self.__kilometers} kilometers")
        else:
            print("the system is off, you can't see, please put on system")



if __name__ == '__main__':
        bolt = ElectroScooterBolt()



