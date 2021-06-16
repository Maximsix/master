# data types


# 1 task
john_salary = 1000.0
marta_salary = 750.0

print(john_salary)
print(marta_salary)

# 2 task
john_age = 25
marta_age = 24

print(john_age)
print(marta_age)


# 3 task
john_name = 'john is good boy'
marta_name = 'marta is good girl'

print(john_name)
print(marta_name)


# task 4

john_gender = True
marta_gender = False

print(john_gender)
print(marta_gender)

# task 5

john_friends = ['Addelyn', 'Jason', 'Maksim']
marta_friends = ['Jennifer', 'William', 'Troy']


print(john_friends)
print(marta_friends)

# task 6
name_list = ['Addelyn', 'Jason', 'Jennifer', 'Addelyn', 'Jason', 'Jennifer']

print(set(name_list))


# 7 task
john_coordinates = (50.438905,30.597014)
marta_coordinates = (50.438905,30.597014)

print(john_coordinates)
print(marta_coordinates)

# task 8
john = {'full_name': 'John',
        'age': 24,
        'salary': 1500,
        'gender': True,
        'friends': john_friends,
        'coordinates': john_coordinates }

marta = {'full_name': 'Marta',
        'age': 21,
        'salary': 750,
        'gender': False,
        'friends': marta_friends,
        'coordinates': john_coordinates }

print(john)
print(marta)






# task with star

# dict friends for John and Marta

addelyn = {'full_name': 'Addelyn',
        'age': 19,
        'salary': 400,
        'gender': False,
        'friends': marta['full_name'],
        'coordinates':(50.433305,30.590004)
           }

jason = {'full_name': 'Jason',
        'age': 29,
        'salary': 340,
        'gender': True,
        'friends': john['full_name'],
        'coordinates':(50.466605,30.509604)
         }


william = {'full_name': 'William',
        'age': 22,
        'salary': 1345,
        'gender': True,
        'friends': john['full_name'],
        'coordinates':(50.466605,30.509604)
           }

jennifer = {'full_name': 'Jennifer',
        'age': 23,
        'salary': 3000,
        'gender': False,
        'friends': marta['full_name'],
        'coordinates':(50.412305,30.590984)
        }

# update dict friends key value
john = {'full_name': 'John',
        'age': 24,
        'salary': 1500,
        'gender': True,
        'coordinates': john_coordinates,
        'friends': [william, jason]
         }

marta = {'full_name': 'Marta',
        'age': 21,
        'salary': 750,
        'gender': False,
        'coordinates': john_coordinates,
        'friends': [jennifer, addelyn]
         }
print(marta)
print(john)






