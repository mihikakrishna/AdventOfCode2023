# Part 1
lines = open("day1/input.txt", 'r').readlines()
total_part1 = 0

for line in lines:
    digits = [char for char in line if char.isnumeric()]
    if digits:
        firstDigit, lastDigit = int(digits[0]), int(digits[-1])
        total_part1 += 10 * firstDigit + lastDigit
print("Answer to part 1: " + str(total_part1))