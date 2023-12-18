def readInput(filename):
    cardsArray = []
    with open(filename) as file:
        for line in file:
            _, cardLists = line.rstrip().split(":")
            winningCardsList = [int(cardNum) for cardNum in cardLists.split("|")[0].split(" ") if cardNum != '']
            yourCardsList = [int(cardNum) for cardNum in cardLists.split("|")[1].split(" ") if cardNum != '']
            cardsArray.append((winningCardsList, yourCardsList))
    return cardsArray

def getMatchesPerCard(cardPair):
    winningCardsSet, yourCardsSet = set(cardPair[0]), set(cardPair[1])
    matches = 0
    for card in yourCardsSet:
        matches += 1 if card in winningCardsSet else 0
    return matches

def processCards(cardsArray):
    cardInstances = [1 for i in range(len(cardsArray))]
    for i in range(len(cardsArray)):
        cardPair = cardsArray[i]
        matches = getMatchesPerCard(cardPair)
        for j in range(i + 1, i + matches + 1):
            if j == len(cardInstances):
                break
            cardInstances[j] += cardInstances[i]

    return(sum(cardInstances))
        

if __name__ == "__main__":
    cardsArray = readInput("day4/input.txt")
    totalPoints = processCards(cardsArray)
    print(totalPoints)
