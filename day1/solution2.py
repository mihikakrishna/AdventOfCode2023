
def readInput(filename):
    with open(filename) as file:
        return [line.rstrip() for line in file]
    
def findStartingNumber(index: int, inputLine: str, numStrings: list[str]) -> int:
    if inputLine[index].isnumeric():
        return int(inputLine[index])
    for num, numString in enumerate(numStrings):
        if inputLine[index:].startswith(numString):
            return num
    return -1

def getStartingNumber(inputLine, numStrings):
    for i in range(len(inputLine)):
        number = findStartingNumber(i, inputLine, numStrings)
        if number != -1:
            return number
    assert(False)

def findSumOfAllInputStrings(inputList, numStrings):
    totalSum = 0
    reversedNumStrings = [numStr[::-1] for numStr in numStrings]
    for inputString in inputList:
        startingNumber = getStartingNumber(inputString, numStrings)
        endingNumber = getStartingNumber(inputString[::-1], reversedNumStrings)
        totalSum += 10*startingNumber+endingNumber
    return totalSum

if __name__ == "__main__":
    numStrings = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    inputList = readInput("day1/input.txt")
    result = findSumOfAllInputStrings(inputList, numStrings)
    print(result)