import pickle

with open('./test/data/data_file.txt', 'rb') as file:
    bite_text = file.read()
    bite_line_of_numbers = pickle.loads(bite_text)

for index in bite_line_of_numbers:
    if index[2] == 1:
        print(index[0] + index[1])
    elif index[2] == 2:
        print(index[0] - index[1])
    else:
        print(index[0] * index[1])

# bite_line_of_numbers - it is not bytes but python object so you can name it
# like operations
# index - confusing name. Are we get index there?
# Good but it could be write cleaner. Take a look.
# TODO: more readable solution^
#  for operation in operations:
#      left_operand, right_operand, operator = operation
#      if operation == 1:
#          print(left_operand + right_operand)
#      elif operation == 2:
#          print(left_operand - right_operand)
#      else:
#          print(left_operand * right_operand)
