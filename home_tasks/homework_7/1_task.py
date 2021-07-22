from typing import Callable

# test data code
number_list = [1, 2, 3, 4, 5, 6, 7, 8]
names_list = ["John", "Marta", "Jora", "Bob", "Petr"]
function_one = lambda number: number % 2 == 0
function_two = lambda string_name: len(string_name) > 4


def custom_filter(callback: Callable, sequence):
    keeper = []
    type_sequence = type(sequence)
    for element in sequence:
        if callback(element):
            keeper.append(element)
    return type_sequence(keeper)

if __name__ == '__main__':
    john = {"name": "John", "age": 23, "gender": "Male"}
    james = {"name": "James", "age": 12, "gender": "Male"}
    marta = {"name": "Marta", "age": 56, "gender": "Female"}

    print(custom_filter(lambda n: n > 5, [1, 4, 56, 7, 87]))
    print(custom_filter(lambda n: n.startswith('J'), ["James", "Marta", "John"]))
    print(
        custom_filter(
            lambda man: man["name"].startswith('J'),
            [john, james, marta]
        )
    )