import random

input_string = input("What do you want to roll?: ")
split_string = input_string.split("d")
number_of_rolls = int(split_string[0])
d_type = int(split_string[1])
rolls = []
rolls_string = ''

for _ in range(number_of_rolls):
    rolls.append(random.randint(1, d_type))

for i in rolls:
    rolls_string += ', '.join(str(i)) + ' '

print(f"You rolled {sum(rolls)}: {rolls_string}")
    