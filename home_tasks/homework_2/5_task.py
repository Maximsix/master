# new structure
vip_plases = ((1, 'Maksim'), (2, 'Alex'), (3, 'Anthony'), (4, 'Thomas'))


hall_plases = {
    1: 'Alex',
    2: 'George',
    3: 'Oscar',
    4: 'George',
    5: 'Free',
    6: 'Free',
    7: 'Free',
}


# vip_lodge = (vip_plases[1], vip_plases[2], vip_plases[3], vip_plases[4]) # over engineered

common_hall = [hall_plases[1], hall_plases[2], hall_plases[3], hall_plases[4]]








# demonstration
def add_person(take_quantity) -> int:
    name = 0
    take_quantity = int(input('specify no more than 3 persons :'))
    for x in range(take_quantity):
        name = input('enter the name of the guest :')  # blocking operation inside function in syncronouse code it is not the best idea but good enought for demonstration
        for n in hall_plases:
            if hall_plases[n] == 'Free':
                hall_plases[n] = name
                print("one guest was added")
                break
        common_hall.append(hall_plases[5])
    print(common_hall)
    print(hall_plases)

add_person(3)

# you could define vip like ((1, "Johh Dow"), (2, "Marta Stuard"))
