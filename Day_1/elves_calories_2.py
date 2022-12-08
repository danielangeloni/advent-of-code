import sys

max = [0, 0, 0]

f = open("input.txt", "r")
elves = f.read()
f.close() 

elves = elves.split('\n\n')

for elf in elves:
    elf_total = 0

    for food_item in elf.split("\n"):
        elf_total += int(food_item)

    if elf_total > max[2]: 
        max[0] = max[1]
        max[1] = max[2]
        max[2] = elf_total
    elif elf_total > max[1]: 
        max[0] = max[1]
        max[1] = elf_total
    elif elf_total > max[0]: 
        max[0] = elf_total
    
    max.sort()

print(max[0] + max[1] + max[2])