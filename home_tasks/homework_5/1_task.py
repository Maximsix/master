from random import *
import os
import pickle

some_file = 'data_file.txt'
list_of_tuples_with_numbers = [tuple(result for result in [randint(1,1000), randint(1,1000), randint(1,3)]) for row in range(100)]

os.makedirs('./test/data')
os.chdir('test/data')
os.system(f"touch {some_file}")

with open(some_file, 'wb') as file:
    data_with_numbers = pickle.dumps(list_of_tuples_with_numbers)
    file.write(data_with_numbers)

