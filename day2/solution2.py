def read_input(filename):
    games = []
    with open(filename) as file:
        for line in file:
            game, pulls = line.rstrip().split(": ")
            gameId = int(game[5:])
            rounds = [
                [(int(count), color) for count, color in (cube.split() for cube in pull.split(", "))]
                for pull in pulls.split("; ")
            ]
            games.append((gameId, rounds))
    return games

def check_if_valid(line):
    _, pulls = line
    max_counts = {'red': 0, 'blue': 0, 'green': 0}
    for pull in pulls:
        for count, color in pull:
            max_counts[color] = max(max_counts[color], count)
    return max_counts['red'] * max_counts['blue'] * max_counts['green']

if __name__ == "__main__":
    input_list = read_input("day2/input.txt")
    print(sum(check_if_valid(line) for line in input_list))
