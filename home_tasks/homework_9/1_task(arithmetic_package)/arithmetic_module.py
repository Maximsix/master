

def addition(first_operand: int, second_operand: int) -> int:
    return first_operand + second_operand

def subtraction(first_operand: int, second_operand: int) -> int:
    return first_operand - second_operand

def integer_division(first_operand: int, second_operand: int) -> int:
    return first_operand // second_operand


if __name__ == '__main__':
    print(addition(99, 1))
    print(subtraction(100, 1))
    print(integer_division(100, 10))