import string

f = open("/home/daniel/Desktop/work/Advent_Of_Code/Day_3/input", "r")
rucksacks = f.read()
f.close() 

sum_of_priorities = 0

def get_index(item):
    if item.isupper():
        return (string.ascii_uppercase.index(item)) + 1 + 26
    else:
        return (string.ascii_lowercase.index(item)) + 1


for rucksack in rucksacks.splitlines():
    half = int(len(rucksack)/2)

    first_compartment = rucksack[:half]
    second_compartment = rucksack[-half:]

    common_items = list(set(first_compartment) & set(second_compartment))

    for common_item in common_items:
        sum_of_priorities += get_index(common_item)


print(sum_of_priorities)