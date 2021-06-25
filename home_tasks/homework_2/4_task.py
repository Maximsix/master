vegetarians = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris']
omnivores = ['Tyler Beverly', 'William Ford', 'Brandon Newman', 'George Allen']
vegetarians.extend(omnivores)

for x in vegetarians:
        print(f'{x}, eats vegetables and herbs')

# Good. You choose right type but you shoud not extent existing group of peaple you should create new ont
# print(vegetarians + omnivores)
