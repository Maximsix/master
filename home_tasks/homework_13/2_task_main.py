from MaximGekalo.master.home_tasks.homework_13.train import Train
from MaximGekalo.master.home_tasks.homework_13.train_car import TrainCar

if __name__ == "__main__":
    car_one = TrainCar(777, 25, ["John", "Marta"])
    print(car_one)
    print(len(car_one))
    train_one = Train(1, "passenger train", "Kyiv - Odessa")
    train_one.add_train_car(car_one)
    # works print of train but does not work print of len in train return error
    # print(len(car_one))
    # TypeError: 'list'
    # object is not callable
    # -3 points

    car_one.add_passenger(1)
    # if len(self.__seats_in_car) <= len(self.__passengers + passengers):
    # TypeError: object of type 'int' has no len()
    # -2 points
