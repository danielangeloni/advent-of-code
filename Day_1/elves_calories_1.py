import sys

max = 0

f = open("input.txt", "r")
elves = f.read()
f.close() 

elves = elves.split('\n\n')

for elf in elves:
    elf_total = 0

    for food_item in elf.split("\n"):
        elf_total += int(food_item)

    if elf_total > max: 
        max = elf_total

print(max)