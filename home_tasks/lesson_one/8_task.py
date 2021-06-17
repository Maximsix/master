# task 8

john = {'full_name': 'John',
        'age': 24,
        'salary': 1500,
        'gender': True,
        'friends': john_friends,
        'coordinates': john_coordinates
        }

marta = {'full_name': 'Marta',
        'age': 21,
         'salary': 750,
        'gender': False,
        'friends': marta_friends,
        'coordinates': john_coordinates
         }

# Good but it could be described and printed in console in more elegant way:
# john = {
#     "first_name": "John",
#     "last_name": "Smith",
#     "age": 25,
#     "gender": "male",
#     "parents": ["John Smith Junio", "Marta Smith"]
# }
#  Look on how dict is described. It is more preferable view on real projects.
# print(john)
#
#
# for key, value in john.items():
#     # print(key, value, sep=" => ")
#     print(f"{key} => {value}")

print(john)
print(marta)

# TODO: john_friends and marta friends should be some list with strings like in task 5 look on examples in usefull links for lesson 1 in LMS
# TODO: john_coordinates and marta_coordinates should be some tuple like in task 7
# Unfortunantly this script will not work
