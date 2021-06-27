vegetarians = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
omnivores = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'George Allen']
new_group_people = [vegetarians, omnivores]


for x in new_group_people:
        for n in x:
            print(f'{n}, eats vegetables and herbs')

# Good. You choose right type but you shoud not extent existing group of peaple you should create new ont
# print(vegetarians + omnivores)
