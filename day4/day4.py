# Goal: In a given grid containing either "."(nothing) or "@"(a paper roll according to the lore),
# calculate the total number of paper rolls that has fewer than 4 (< 4) other paper rolls in the adjacent
# cells.
# only need to check the cell that contains "@"

file = open("day4input.txt", "r")
rows = file.read().split("\n")
MAX_ROLLS = 4
A_ROLL = "@"

accessibleCounter = 0
for rowIdx, row in enumerate(rows):
    for cellIdx, cell in enumerate(row):
        if (cell == A_ROLL):
            # for each cell
            rollCounter = 0
            # if previous cell exists -> check
            if (cellIdx > 0 and cellIdx <= len(row) - 1):
                rollCounter += 1 if row[cellIdx - 1] == A_ROLL else 0
            # if next cell extsts -> check
            if(cellIdx == 0 or cellIdx < len(row) - 1):
                rollCounter += 1 if row[cellIdx + 1] == A_ROLL else 0
            # if previous row extsts
            if (rowIdx > 0):
            #   -> check right above
                rollCounter += 1 if rows[rowIdx - 1][cellIdx] == A_ROLL else 0
            #   -> if previous cell exists -> check
                if (cellIdx > 0 and cellIdx <= len(row) - 1):
                    rollCounter += 1 if rows[rowIdx - 1][cellIdx - 1] == A_ROLL else 0
            #   -> if next cell exists -> check
                if(cellIdx == 0 or cellIdx < len(row) - 1):
                    rollCounter += 1 if rows[rowIdx - 1][cellIdx + 1] == A_ROLL else 0
            # if next row extsts
            if (rowIdx < len(row) - 1):
            #   -> check right above
                rollCounter += 1 if rows[rowIdx + 1][cellIdx] == A_ROLL else 0
            #   -> if previous cell exists -> check
                if (cellIdx > 0 and cellIdx <= len(row) - 1):
                    rollCounter += 1 if rows[rowIdx + 1][cellIdx - 1] == A_ROLL else 0
            #   -> if next cell exists -> check
                if(cellIdx == 0 or cellIdx < len(row) - 1):
                    rollCounter += 1 if rows[rowIdx + 1][cellIdx + 1] == A_ROLL else 0
            
            if (rollCounter < MAX_ROLLS):
                accessibleCounter += 1
print(accessibleCounter)
