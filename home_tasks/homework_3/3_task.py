friends = ["John", "Marta", "Morgan", "Maria", "Huang", "James"]
enemies = ["John", "Johnatan", "Artur"]

for index in friends:  # what is index? Maybe better name it like friend?
    if not index in enemies:
        if index == friends[2]:  # what if I don't know where James?
            continue
        print(f"{index} we are the best friends")
    elif index in enemies:
        print(f"{index} we are not the friends anymore")