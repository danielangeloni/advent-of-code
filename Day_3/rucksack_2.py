import string
from itertools import islice

f = open("/home/daniel/Desktop/work/Advent_Of_Code/Day_3/input", "r")
rucksacks = (f.read()).splitlines()
f.close() 
sum_of_priorities = 0
current_index = 0

def get_index(item):
    if item.isupper():
        return (string.ascii_uppercase.index(item)) + 1 + 26
    else:
        return (string.ascii_lowercase.index(item)) + 1


for first, second, third in zip(rucksacks[0:], rucksacks[1:], rucksacks[2:]):
    if current_index % 3 == 0:
        for common_item in list(set(first) & set(second) & set(third)):
            sum_of_priorities += get_index(common_item)
    current_index += 1

print(sum_of_priorities)