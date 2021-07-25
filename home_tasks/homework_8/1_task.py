from typing import Generator


def search_square_root_gen() -> Generator:
    square_root = (item ** 2 for item in range(1000000001) if item % 2 == 0)
    return square_root


for element in search_square_root_gen():
    print(element)
