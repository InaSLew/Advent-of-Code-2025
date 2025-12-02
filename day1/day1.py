file = open("day1input.txt", "r")
inputs = file.read().split("\n")

DECREASE = "L"
TOTAL_NUMBER_DIAL = 100 # 0 - 99 -> 100 dials
LOWEST_DIAL = 0
HIGHEST_DIAL = 99
truePassword = 0
currentNumber = 50

for input in inputs:
    direction = input[0]
    clicks = int(input[1:])
    currentNumber = currentNumber - clicks if direction == DECREASE else currentNumber + clicks

    if (currentNumber < LOWEST_DIAL) :
       currentNumber = TOTAL_NUMBER_DIAL - (abs(currentNumber) % TOTAL_NUMBER_DIAL)
    if (currentNumber > HIGHEST_DIAL) :
       currentNumber = (currentNumber % TOTAL_NUMBER_DIAL)
    
    if (currentNumber == 0) :
        truePassword += 1
    
print(truePassword)