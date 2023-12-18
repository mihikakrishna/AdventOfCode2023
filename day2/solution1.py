RED = 12
GREEN = 13
BLUE = 14

def read_input(filename):
    games = []
    with open(filename) as file:
        for line in file:
            game, grabs = line.rstrip().split(": ")
            gameId = int(game[5:])
            rounds = [
                [(int(count), color) for count, color in (cube.split() for cube in grab.split(", "))]
                for grab in grabs.split("; ")
            ]
            games.append((gameId, rounds))
    return games

def check_if_valid(line):
    gameId, pulls = line
    for pull in pulls:
        for count, color in pull:
            if (color == "green" and count > GREEN) or \
               (color == "red" and count > RED) or \
               (color == "blue" and count > BLUE):
                return 0
    return gameId

if __name__ == "__main__":
    input_list = read_input("day2/input.txt")
    print(sum(check_if_valid(line) for line in input_list))
