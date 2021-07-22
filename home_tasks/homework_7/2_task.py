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
    print(custom_map(function_one, number_list))