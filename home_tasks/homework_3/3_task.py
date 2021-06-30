

friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for index in friends:
    if not index in enemies:
        if index == friends[2]:
            continue
        print(f"{index} we are the best friends")
    elif index in enemies:
        print(f"{index} we are not the friends anymore")