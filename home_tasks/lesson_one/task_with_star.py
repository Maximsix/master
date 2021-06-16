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