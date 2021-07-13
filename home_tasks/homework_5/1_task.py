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

# Good. As alternative you can write bytes in 1 line into the file using dump
# pickle.dump(list_of_tuples_with_numbers, file)

# TODO: resolve next warning of PEP8
#  1_task.py:1:1: F403 'from random import *' used; unable to detect undefined names
#  1_task.py:6:60: F405 'randint' may be undefined, or defined from star imports: random
#  1_task.py:6:69: E231 missing whitespace after ','
#  1_task.py:6:77: F405 'randint' may be undefined, or defined from star imports: random
#  1_task.py:6:80: E501 line too long (130 > 79 characters)
#  1_task.py:6:86: E231 missing whitespace after ','
#  1_task.py:6:94: F405 'randint' may be undefined, or defined from star imports: random
#  1_task.py:6:103: E231 missing whitespace after ','
