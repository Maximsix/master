from typing import Callable

# test data code
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names_list = ["John", "Marta", "Jora", "Bob", "Petr"]
function_one = (lambda a, n: a + n)
function_two = (lambda a, n: a if a > n else n)
function_three = (lambda a, n: a if a < n else n)

def custom_reduce(callback: Callable, sequence):
    element = sequence[0]
    counter = 0
    for _ in sequence:
        if len(sequence) - 1 == counter:
            break
        counter += 1
        element = callback(element, sequence[counter])
    return element

if __name__ == '__main__':
    print(custom_reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]))
    print(custom_reduce(lambda a, b: a if a > b else b, [1, 2, 3, 4, 5]))
    print(custom_reduce(lambda a, b: a if a < b else b, [1, 2, 3, 4, 5]))
    print(custom_reduce(lambda a, b: a + b, ["One", "Two"]))
