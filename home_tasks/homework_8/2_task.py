from typing import Union


def output_called_function(func):
    def inner(*args, **kwargs):
        return f'{func.__name__}\n{func(*args, **kwargs)}'
    return inner


@output_called_function
def shape_numbers(number_one: Union[int, float], number_two: Union[int, float]) -> Union[int, float]:
    result = number_one + number_two
    return result


@output_called_function
def multiplication_of_numbers(number_one: Union[int, float], number_two: Union[int, float]) -> Union[int, float]:
    result = number_one * number_two
    return result


if __name__ == '__main__':
    print(5 + multiplication_of_numbers(1, 4))

# Well seems like your decorator brake main logic of function
#     print(5 + multiplication_of_numbers(1, 4))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# -5 points