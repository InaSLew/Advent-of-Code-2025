
DECREASE = "L"

file = open("day1input.txt", "r")
inputs = file.read().split("\n")

startNumber = 50
truePassword = 0
for input in inputs:
    direction = input[0]
    clicks = int(input[1:])
    numberOnDial = startNumber + (-clicks) if direction == DECREASE else clicks
    if numberOnDial == 0 :
        truePassword += 1
    else :
        numberOnDial = 99 - (numberOnDial - 1) if numberOnDial < 0 else (numberOnDial - 1) - 99
    startNumber = numberOnDial
        
print(truePassword)