import math
from itertools import permutations

N = int(input())
number = []
for i in input().split(" "):
    number.append(int(i))
line = input().split(" ")
val = []
for i in range(4):
    temp = int(line[i])
    for j in range(temp):
        val.append(i)
minAnswer = math.inf
maxAnswer = -math.inf
tempNum = number[0]
resultVal = set(permutations(val, len(val)))
for value in resultVal:
    for j in range(len(value)):
        if value[j] == 0:
            tempNum += number[j + 1]
        elif value[j] == 1:
            tempNum -= number[j + 1]
        elif value[j] == 2:
            tempNum *= number[j + 1]
        else:
            tempNum = int(tempNum / number[j + 1])

    minAnswer = min(minAnswer, tempNum)
    maxAnswer = max(maxAnswer, tempNum)
    tempNum = number[0]

print(maxAnswer)
print(minAnswer)
