from home_tasks.homework_13.train import Train
from home_tasks.homework_13.train_car import TrainCar

if __name__ == '__main__':
    car_one = TrainCar(777, 25, ['John', 'Marta'])
    print(car_one)
    train_one = Train(1, 'passenger train', 'Kyiv - Odessa')
    train_one.add_train_car(car_one)

