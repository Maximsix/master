from typing import Callable, Collection

# test data code
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names_list = ["John", "Marta", "Jora", "Bob", "Petr"]
function_one = (lambda num: str(num))
function_two = (lambda num: str(num).title() )

def custom_map(callback: Callable, sequence):
    keeper = []
    type_sequence = type(sequence)
    for element in sequence:
        keeper.append(callback(element))
    return type_sequence(keeper)

if __name__ == '__main__':
    john = {"name": "John", "age": 23, "gender": "Male"}
    james = {"name": "James", "age": 12, "gender": "Male"}
    marta = {"name": "Marta", "age": 56, "gender": "Female"}

    print(custom_map(lambda n: n ** 2, [1, 4, 56, 7, 87]))
    print(custom_map(lambda n: f"Hello {n}", ["James", "Marta", "John"]))
    print(
        custom_map(
            lambda man: (man["name"], man["age"]),
            [john, james, marta]
        )
    )