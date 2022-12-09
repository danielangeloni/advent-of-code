f = open("Day_4/input", "r")
ids = f.read()
f.close() 

counter = 0

for pair in ids.splitlines():
    first_pair = []
    second_pair = []
    
    for single in pair.split(","):
        temp_pair = []
        half_single = single.split("-")

        for i in range(int(half_single[0]), int(half_single[1]) + 1):
            temp_pair.append(str(i)) 

        if not first_pair:
            first_pair = temp_pair
        else:
            second_pair = temp_pair

    if list(set(first_pair) & set(second_pair)):
        counter += 1

print(counter)