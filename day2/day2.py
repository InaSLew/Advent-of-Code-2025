# Goal: identifying any number in a given range that when stringfied and split in half, its first and second half are identical.
# Cible : Identifier tous les numéros dans les séries numériques dont, quand découpés en moitié, la première partie est identique à la deuxième.
# Piège -> le paramètre de stop dans la fonction range(start, stop, step)

file = open("day2input.txt", "r")
inputs = file.read().split(",")

invalidIDSum = 0

for input in inputs:
    firstLastIDList = input.split("-")
    firstID = int(firstLastIDList[0])
    lastID = int(firstLastIDList[1])
    for productID in range(firstID, lastID + 1):
        productIDStr = str(productID)
        productIDLen = len(productIDStr)
        if (productIDLen % 2 == 0 and productIDStr[0: (1 if productIDLen // 2 == 1 else productIDLen // 2)] == productIDStr[productIDLen // 2:]):
            invalidIDSum += productID

print(invalidIDSum)