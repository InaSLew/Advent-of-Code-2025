# Part 1
# Goal: Identify the highest-valued two-digit combo in a given sequance of numbers ranging from 1 to 9;
# the second digit in the combo must come after the first digit in order in the given sequance, so consider the following sequance:
# "818181911112111", 92 would be the correct highest-valued combo instead of 98, as its construction is against the rule described above.

file = open("day3input.txt", "r")
inputs = file.read().split("\n")

outputJoltageSum = 0
for input in inputs:
    firstDigit = 0
    secondDigit = 0
    newStartIdx = 0
    lastIdx = len(input) - 1
    for idx, digit in enumerate(input) :
        voltage1 = int(digit)
        if (voltage1 > firstDigit and idx < lastIdx): # firstDigit CANNOT be in the last position of the sequance.
            firstDigit = voltage1
            newStartIdx = idx + 1 # modifying the newStartIdx here instead of while picking out secondDigit apparently did the trick? wtf?
    for idx, digit in enumerate(input[newStartIdx:]):
        voltage2 = int(digit)
        secondDigit = voltage2 if voltage2 > secondDigit else secondDigit
    outputJoltageSum += int(str(firstDigit)+str(secondDigit))
    

print(outputJoltageSum)

