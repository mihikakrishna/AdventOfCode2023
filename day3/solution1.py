
def readInput(filename):
    with open(filename) as file:
        return [[char for char in line.rstrip()] for line in file]

def findSymbolCoordinates(inputMatrix):
    symbolCoordinates = []
    for r in range(len(inputMatrix)):
        for c in range(len(inputMatrix[0])):
            if not inputMatrix[r][c].isalnum() and inputMatrix[r][c] != ".":
                symbolCoordinates.append((r, c))
    return symbolCoordinates

def searchAdjacentCellsForNumbers(inputMatrix, r, c):
    directions = [0, 1, -1]
    currentPartNumberSum = 0

    for dr in directions:
        for dc in directions:
            if inputMatrix[r + dr][c + dc].isnumeric():
                currentPartNumberSum += getPartNumber(inputMatrix, r + dr, c + dc)
    return currentPartNumberSum

def getPartNumber(inputMatrix, r, c):
    while inputMatrix[r][c].isnumeric():
        c -= 1
    
    numStr = ""
    c += 1

    while c < len(inputMatrix[0]) and inputMatrix[r][c].isnumeric():
        numStr += inputMatrix[r][c]
        inputMatrix[r][c] = "."
        c += 1

    return int(numStr)


if __name__ == "__main__":
    inputMatrix = readInput("day3/input.txt")
    symbolCoordinates = findSymbolCoordinates(inputMatrix)
    sumOfPartNumbers = 0
    for (r, c) in symbolCoordinates:
        sumOfPartNumbers += searchAdjacentCellsForNumbers(inputMatrix, r, c)

    print(sumOfPartNumbers)