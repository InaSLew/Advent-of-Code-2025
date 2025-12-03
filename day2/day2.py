file = open("test.txt", "r")
inputs = file.read().split(",")

invalidIDSum = 0

# part 1
# Goal: identifying any number in a given range that when stringfied and split in half, its first and second half are identical.
# Cible : Identifier tous les numéros dans les séries numériques dont, quand découpés en moitié, la première partie est identique à la deuxième.
# Piège -> le paramètre de stop dans la fonction range(start, stop, step)
# for input in inputs:
#     firstLastIDList = input.split("-")
#     firstID = int(firstLastIDList[0])
#     lastID = int(firstLastIDList[1])
#     for productID in range(firstID, lastID + 1):
#         productIDStr = str(productID)
#         productIDLen = len(productIDStr)
#         if (productIDLen % 2 == 0 and productIDStr[0: (1 if productIDLen // 2 == 1 else productIDLen // 2)] == productIDStr[productIDLen // 2:]):
#             invalidIDSum += productID

# part 2
# 4174379265
# 1303733892002 - too high
# problems: 565656 and 1001
lookup = dict()
for input in inputs:
        firstLastIDList = input.split("-")
        firstID = int(firstLastIDList[0])
        lastID = int(firstLastIDList[1])
        for productID in range(firstID, lastID + 1):
            productIDStr = str(productID)
            productIDLen = len(productIDStr)
            if (productIDLen % 2 == 0 and productIDStr[0: (1 if productIDLen // 2 == 1 else productIDLen // 2)] == productIDStr[productIDLen // 2:]):
                print(productID)
                invalidIDSum += productID
            else:
                for digit in productIDStr:
                    lookup[digit] = 1 if (digit not in lookup) else lookup[digit] + 1
                if (len(set(lookup.values())) == 1 and set(lookup.values()).pop() > 1) :
                    print(productID)
                    invalidIDSum += productID
                lookup.clear()

print("result: ", invalidIDSum)