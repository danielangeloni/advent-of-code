
f = open("/home/daniel/Desktop/work/Advent_Of_Code/Day_2/input", "r")
guide = f.read()
f.close() 

# ROCK A 
# PAPER B
# SCISSORS C

# WIN Z
# LOSE X
# DRAW Y


def move_point_value(move):
    if move == 'A' or move == "X":
        return 1
    if move == 'B' or move == "Y":
        return 2
    if move == 'C' or move == "Z":
        return 3

def move(move):
    score = 0

    player_1_win = ["AB", "CA", "BC"]
    draw = ["AA", "BB", "CC"]
    player_1_loss = ["AC", "BA", "CB"]

    # WIN
    if move[1] == 'Z':
        shapes = player_1_win
        score += 6
    # LOSE
    elif move[1] == 'X':
        shapes = player_1_loss
    # DRAW
    if move[1] == 'Y':
        shapes = draw
        score += 3

    for shape in shapes:
        if shape[0] == move[0]:
            chosen_shape = shape
            break

    score += move_point_value(chosen_shape[1])

    return score

total_score = 0
for round in guide.splitlines():
    moves = round.split(" ")
    total_score += move(moves)

print(total_score)