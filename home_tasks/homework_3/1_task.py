# # example 1

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# counter = 0
# even_list1 = []
# odd_list1 = []
# for index in numbers_list:
#     if index % 2 == 0:
#         even_list1.append((f'index {counter}', f' value {index}'))
#         counter += 1
#     else:
#         odd_list1.append((f'index {counter}', f' value {index}'))
#         counter += 1
# else:
#     print('Even list')
#     for x in even_list1:
#         print(''.join(list(x)))
#     print('\nOdd list')
#     for x in odd_list1:
#         print(''.join(list(x)))



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

# well it is good but tuple should be with 2 digits instead of 2 strings.
# take a look on alternative solutions
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# numbers_with_odd_index = []
# numbers_with_event_index = []
#
# for index, value in enumerate(numbers):
#     if bin(index)[-1] == '1':
#         numbers_with_odd_index.append((index, value))
#     else:
#         numbers_with_event_index.append((index, value))
#
# print(numbers_with_event_index)
# print(numbers_with_odd_index)
# # or
# some_list = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_list_of_tuples = []
# even_list_of_tuples = []
#
# for index, value in enumerate(some_list):
#     if index % 2 == 0:
#         even_list_of_tuples.append((index, value))
#     else:
#         odd_list_of_tuples.append((index, value))