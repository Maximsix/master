import re

variable_list = ["FirstItem", "FriendsList", "MyTuple"]
text_look_for = re.findall(r'[A-Z][a-z]',''.join(variable_list))
snake_case_list = []
counter1 = 0
counter2 = 1

for x in text_look_for:
    snake_case_list.append(str(text_look_for[counter1] + '_' + text_look_for[counter2]).lower())
    counter1 += 2
    counter2 += 2
    if counter2 >= len(text_look_for) or counter1 >= len(text_look_for):
        break
print(snake_case_list)

