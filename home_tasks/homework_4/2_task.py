names = ["John", "Marta", "James", "Amanda", "Marianna"]

print('Names'.center(25, '*'))
for name in names:
    print(f"{name:>25}")

# Nice. As I can see it is only formatting with fstring but should be second solution too with string methods.
# -2points