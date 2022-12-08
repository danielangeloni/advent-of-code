f = open("/home/daniel/Desktop/work/Advent_Of_Code/Day_2/input", "r")
guide = f.read()
f.close() 

# ROCK
# - AX 
# PAPER
# - BY
# SCISSORS
# - CZ

def move_point_value(move):
    if move == 'A' or move == "X":
        return 1
    if move == 'B' or move == "Y":
        return 2
    if move == 'C' or move == "Z":
        return 3

def move(game_move):
    player_1_win = ["AY", "CX", "BZ"]
    draw = ["AX", "BY", "CZ"]

    score = 0

    move = game_move[0] + game_move[1]

    if move in player_1_win:
        score += 6
    if move in draw:
        score += 3

    score += move_point_value(move[1])

    return score


total_score = 0

for game_round in guide.splitlines():
    moves = game_round.split(" ")
    total_score += move(moves)

print(total_score)