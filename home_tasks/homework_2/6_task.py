people = ['Maksim Gekalo', 'Alex Wallace', 'Anthony Labert','Thomas Harris','Alex Wallace','Maksim Gekalo']



# example 1
unique = []
for name in people:
    if name in unique:
        continue
    else:
        unique.append(name)
print(unique)

# example 2
print(list(frozenset(people)))

# Good. Interesting solution but it could be done with dicts
# print(list({}.fromkeys(people).keys()))
