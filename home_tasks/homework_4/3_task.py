import re

some_string = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                                       "
new_str = some_string.strip()
modified_string = re.split(r"&{1,2}|\s", new_str)
list1 = []
list2 = []
dict_keys_values = {}

for index in modified_string:
    list1.append(index.split("=", 1))
for list_index in list1:
    for b in list_index:
        list2.append(b)
dict_key_value = dict(zip(list2[::2], list2[1::2]))
print(dict_key_value)

# It is really good but take a look how it could be make cleaner.
# result = dict()
#
# for pair in some_string.strip().split('&'):
#     if pair:
#         key, value = pair.split('=', maxsplit=1)
#         result[key] = value
#
# print(result)
