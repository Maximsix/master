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

