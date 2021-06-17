# task with star

# dict friends for John and Marta

addelyn = {'full_name': 'Addelyn',
        'age': 19,
        'salary': 400,
        'gender': False,
        'friends': marta['full_name'],  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
        'coordinates':(50.433305,30.590004)
           }

jason = {'full_name': 'Jason',
        'age': 29,
        'salary': 340,
        'gender': True,
        'friends': john['full_name'],  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
        'coordinates':(50.466605,30.509604)
         }


william = {'full_name': 'William',
        'age': 22,
        'salary': 1345,
        'gender': True,
        'friends': john['full_name'],  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
        'coordinates':(50.466605,30.509604)
           }

jennifer = {'full_name': 'Jennifer',
        'age': 23,
        'salary': 3000,
        'gender': False,
        'friends': marta['full_name'],  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
        'coordinates':(50.412305,30.590984)
        }

# update dict friends key value
john = {'full_name': 'John',
        'age': 24,
        'salary': 1500,
        'gender': True,
        'coordinates': john_coordinates, # seems like it was in common module at first so I suppose if it was tuple there is it also good
        'friends': [william, jason]  # Good here
         }

marta = {'full_name': 'Marta',
        'age': 21,
        'salary': 750,
        'gender': False,
        'coordinates': john_coordinates, # little bit strange that marta has coordinates of john but it is OK
        'friends': [jennifer, addelyn]
         }
print(marta)
print(john)


# Unfortunately this script will not work. Ask your lead if requirements are not clear or confuse.
