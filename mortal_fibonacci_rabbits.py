def rabbitPairs(numMonths, numOffspring):
    if (numMonths == 1):
        return 1

    elif (numMonths == 2):
        return numOffspring

    oneGen = rabbitPairs(numMonths - 1, numOffspring)
    twoGen = rabbitPairs(numMonths - 2, numOffspring)
    if (numMonths <= 4):
        return (oneGen + twoGen)

    return (oneGen + (twoGen * numOffspring))


print(rabbitPairs(5, 3))