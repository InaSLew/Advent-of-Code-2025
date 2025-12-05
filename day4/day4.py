# Goal: In a given grid containing either "."(nothing) or "@"(a paper roll according to the lore),
# calculate the total number of paper rolls that has fewer than 4 (< 4) other paper rolls in the adjacent
# cells.
# only need to check the cell that contains "@"

file = open("day4input.txt", "r")
rows = file.read().split("\n")
MAX_ROLLS = 4
A_ROLL = "@"

def checkAdjacentCells(CellIndex, RowIndex, Rows):
    counter = 0
    # if previous cell exists -> check
    if (CellIndex > 0 and CellIndex <= len(Rows[RowIndex]) - 1):
        counter += 1 if Rows[RowIndex][cellIdx - 1] == A_ROLL else 0
    # if next cell extsts -> check
    if(cellIdx == 0 or cellIdx < len(row) - 1):
        counter += 1 if Rows[RowIndex][cellIdx + 1] == A_ROLL else 0
    return counter

accessibleCounter = 0
for rowIdx, row in enumerate(rows):
    for cellIdx, cell in enumerate(row):
        if (cell == A_ROLL): # for each cell that contains "@"
            rollCounter = 0
            rollCounter += checkAdjacentCells(cellIdx, rowIdx, rows) # check current row
            if (rowIdx > 0): # if previous row exists
                rollCounter += 1 if rows[rowIdx - 1][cellIdx] == A_ROLL else 0 # check the cell right above
                rollCounter += checkAdjacentCells(cellIdx, rowIdx - 1, rows)
            if (rowIdx < len(row) - 1): # if next row exists
                rollCounter += 1 if rows[rowIdx + 1][cellIdx] == A_ROLL else 0 # check the cell right above
                rollCounter += checkAdjacentCells(cellIdx, rowIdx + 1, rows)
            
            if (rollCounter < MAX_ROLLS):
                accessibleCounter += 1
print(accessibleCounter)
