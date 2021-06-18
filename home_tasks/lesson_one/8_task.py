# task 8

john = {
    'full_name': 'John',
    'age': 24,
    'salary': 1500,
    'gender': True,
    'friends': ['Addelyn', 'Jason', 'Maksim'],
    'coordinates': (50.438905, 30.597014)
}

marta = {
    'full_name': 'Marta',
    'age': 21,
    'salary': 750,
    'gender': False,
    'friends': ['Jennifer', 'William', 'Troy'],
    'coordinates': (50.438905, 30.597014)
}

# Good but it could be described and printed in console in more elegant way:
# john = {
#     "first_name": "John",
#     "last_name": "Smith",
#     "age": 25,
#     "gender": "male",
#     "parents": ["John Smith Junio", "Marta Smith"]
# }
# Look on how dict is described. It is more preferable view on real projects.
# print(john)
# Thank's for advice
#
# for key, value in john.items():
#     # print(key, value, sep=" => ")
#     print(f"{key} => {value}")

# I tried this option number one
# def output_information(some_dict) -> dict:
#     for key, value in some_dict.items():
#          print("{} => {}".format(key, value))
#
# output_information(john)
# output_information(marta)
#
#
#
# I tried this option number two, it was fun
#
# def output_information(some_dict) -> dict:
#     for key, value in some_dict.items():
#         for substring in str(key):
#             if substring == "_":
#                 str_key = str(key).replace(substring, " ")
#                 break
#             elif not '_' in key:
#                 str_key = key
#                 break
#         print('%s => %s' % (str_key, value))
#
# output_information(john)
# output_information(marta)
#
#
# final result
#
for key, value in john.items():
    print(f'{key} => {value}')






# TODO: john_friends and marta friends should be some list with strings like in task 5 look on examples in usefull links for lesson 1 in LMS
# TODO: john_coordinates and marta_coordinates should be some tuple like in task 7
# Unfortunantly this script will not work
# i fixed those problems
