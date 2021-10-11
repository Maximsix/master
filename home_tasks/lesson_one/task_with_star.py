william = {
    "full_name": "William",
    "age": 22,
    "salary": 1345,
    "gender": True,
    "friends": None,
    "coordinates": (50.466605, 30.509604),
}


addelyn = {
    "full_name": "Addelyn",
    "age": 19,
    "salary": 400,
    "gender": False,
    "friends": [william],
    "coordinates": (50.433305, 30.590004),
}


john = {
    "full_name": "John",
    "age": 24,
    "salary": 1500,
    "gender": True,
    "coordinates": (50.438905, 30.597014),
    "friends": [addelyn, william],
}


jason = {
    "full_name": "Jason",
    "age": 29,
    "salary": 340,
    "gender": True,
    "friends": [john],
    "coordinates": (50.466605, 30.509604),
}


jennifer = {
    "full_name": "Jennifer",
    "age": 23,
    "salary": 3000,
    "gender": False,
    "friends": [john],
    "coordinates": (50.412305, 30.590984),
}


marta = {
    "full_name": "Marta",
    "age": 21,
    "salary": 750,
    "gender": False,
    "coordinates": (50.438905, 30.597014),
    "friends": [jennifer, addelyn],
}


for key, value in john.items():
    print(f"{key} => {value}")

for key, value in marta.items():
    print(f"{key} => {value}")
