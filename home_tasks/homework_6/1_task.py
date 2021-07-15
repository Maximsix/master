
def arithmetic(left_operand: int, right_operand: int, operation: str):
    '''
        Apply arithmetic operation for provided left and right operands
    '''
    if operation == '+':
        return left_operand + right_operand
    elif operation == '-':
        return left_operand - right_operand
    elif operation == '*':
        return left_operand * right_operand
    elif operation == '/':
        return left_operand / right_operand
    return f'Not known operation: {operation}'
