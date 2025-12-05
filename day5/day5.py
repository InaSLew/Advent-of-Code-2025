# Goal: given a two-part dataset (part 1 and part 2 henceforth) separated by a blank line,
# count the total sum of numbers in part 2 that is within ANY of the number ranges presented
#  in part 1.

data = open("day5input.txt", "r").read().split("\n\n")

freshIDs = data[0].splitlines()
produces = [int(p) for p in data[1].splitlines()]
def getFreshIDs(rangeStr):
    ranges = [int(d) for d in rangeStr.split("-")]
    start = ranges[0]
    end = ranges[1]
    return range(start, end + 1)

counter = 0
for p in produces:
    isFresh = False
    for ID in freshIDs:
        isFresh = p in getFreshIDs(ID)
        if (isFresh):
            counter += 1
            break
print(counter)
