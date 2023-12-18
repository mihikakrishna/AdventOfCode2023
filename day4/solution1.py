def readInput(filename):
    cardsArray = []
    with open(filename) as file:
        for line in file:
            _, cardLists = line.rstrip().split(":")
            winningCardsList = [int(cardNum) for cardNum in cardLists.split("|")[0].split(" ") if cardNum != '']
            yourCardsList = [int(cardNum) for cardNum in cardLists.split("|")[1].split(" ") if cardNum != '']
            cardsArray.append((winningCardsList, yourCardsList))
    return cardsArray

def getPointsPerCard(cardPair):
    winningCardsSet, yourCardsSet = set(cardPair[0]), set(cardPair[1])
    matches = 0
    for card in yourCardsSet:
        matches += 1 if card in winningCardsSet else 0
    
    return int(2 ** (matches - 1))

if __name__ == "__main__":
    cardsArray = readInput("day4/input.txt")
    totalPoints = 0
    for cardPair in cardsArray:
        totalPoints += getPointsPerCard(cardPair)
    print(totalPoints)
