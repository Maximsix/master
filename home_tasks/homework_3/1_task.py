# # example 1

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

counter = 0
even_list1 = []
odd_list1 = []
for index in numbers_list:
    if index % 2 == 0:
        even_list1.append((f'index {counter}', f' value {index}'))
        counter += 1
    else:
        odd_list1.append((f'index {counter}', f' value {index}'))
        counter += 1
else:
    print('Even list')
    for x in even_list1:
        print(''.join(list(x)))
    print('\nOdd list')
    for x in odd_list1:
        print(''.join(list(x)))



# # example 2



numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

even_list2 = []
odd_list2 = []
counter = 0
for index in numbers_list:
    if not index & 1:
        even_list2.append((f'index {counter}', f' value {index}'))
        counter += 1
    else:
        odd_list2.append((f'index {counter}', f' value {index}'))
        counter += 1
else:
    print('Even list')
    for x in even_list2:
        print(''.join(list(x)))
    print('\nOdd list')
    for x in odd_list2:
        print(''.join(list(x)))


