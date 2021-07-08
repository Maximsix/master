names = "john marta james Morgan Adam Maria huang"

# example 1
names_list= []
for x in names.split():
     names_list.append(x.capitalize())
print(names_list)

# example 2
new_names = ', '.join(names_list)
print(new_names)