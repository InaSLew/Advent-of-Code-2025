# Part 1 Goal: Given a 2D array dataset that is made of athrimetic operation signs (either '+' or '*') in the last row,
# and integers in all other rows, calculate the total sum of the result from every column's arithmetic operation.
# You can assume that no data is missing and that every row has equal length.

import math

PLUS_OPERATION = '+'
data = [l. split() for l in open('day6input.txt', 'r').read().splitlines()]
lookup = dict()

# Reorganise the data
for idx,r in enumerate(data):
    for col, i in enumerate(r):
        # lookup[col] = [i] if col not in lookup else lookup[col].append(i) is apparently not the same as the if-else statements below????
        if (col not in lookup):
            lookup[col] = [i]
        else:
            lookup[col].append(i)
counter = 0
columns = lookup.values()
for c in columns: # do the math!
    counter += sum([int(n) for n in c[:-1]]) if c[-1] == PLUS_OPERATION else math.prod([int(n) for n in c[:-1]])
print(counter)





# example = '''123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  '''
# data = [l.split() for l in example.splitlines()]