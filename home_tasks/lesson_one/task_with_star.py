# task with star


# He is bad boy and he doesn't have friends  :(
william = {
    'full_name': 'William',
    'age': 22,
    'salary': 1345,
    'gender': True,
    'friends': None,  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
    'coordinates':(50.466605, 30.509604)
}




addelyn = {
    'full_name': 'Addelyn',
    'age': 19,
    'salary': 400,
    'gender': False,
    'friends': [william],  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
    'coordinates':(50.433305, 30.590004)
}


john = {
    'full_name': 'John',
    'age': 24,
    'salary': 1500,
    'gender': True,
    'coordinates': (50.438905, 30.597014), # seems like it was in common module at first so I suppose if it was tuple there is it also good
    'friends': [addelyn, william]  # Good here
}






jason = {
    'full_name': 'Jason',
    'age': 29,
    'salary': 340,
    'gender': True,
    'friends': [john],  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
    'coordinates':(50.466605, 30.509604)
}


jennifer = {
    'full_name': 'Jennifer',
    'age': 23,
    'salary': 3000,
    'gender': False,
    'friends': [john],  # You can use list with single item like [marta] but marta should be defined before that or you can say that jeniffer has not friends.
    'coordinates':(50.412305, 30.590984)
}



marta = {
    'full_name': 'Marta',
    'age': 21,
    'salary': 750,
    'gender': False,
    'coordinates': (50.438905, 30.597014), # little bit strange that marta has coordinates of john but it is OK
    'friends': [jennifer, addelyn]
}




for key, value in john.items():
    print(f'{key} => {value}')

for key, value in marta.items():
    print(f'{key} => {value}')


# Unfortunately this script will not work. Ask your lead if requirements are not clear or confuse.
# I think, I needed to create Marta's and John's friends without the close friends