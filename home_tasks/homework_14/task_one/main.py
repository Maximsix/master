
from human import Human

if __name__ == '__main__':
    marta = Human("Marta", 20, False)
    john = Human("John", 13, True)
    bob = Human("John", 22, True)

    objects = [marta, john, bob]

for object in objects:
    print(object.drink_alcohol)
