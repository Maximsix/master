vegetarians = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
omnivores = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'George Allen']
new_group_people = [vegetarians, omnivores]


for x in new_group_people:
        for n in x:
            print(f'{n}, eats vegetables and herbs')

# Good. You choose right type but you shoud not extent existing group of peaple you should create new ont
# print(vegetarians + omnivores)

# Good but if you will print new_gourp_people you will get matrix instead of vector.
# print(new_group_people)

# printing it is ok but you should create new list with proper structure
# Also what is 'x' variable what does it mean?
# What is 'n' variable what does it mean. Rename both of them.
# only single variable in system can be named with single symbol '_'
