from itertools import permutations


def solution(expression):
    value = ["+", "-", "*"]
    vallist = list(permutations(value))
    numlist = []
    temp = ""
    answer = 0
    for i in range(len(expression)):
        if expression[i] == "*" or expression[i] == "-" or expression[i] == "+":
            numlist.append(temp)
            numlist.append(expression[i])
            temp = ""
        else:
            temp += expression[i]
        if i == len(expression) - 1:
            numlist.append(temp)

    for i in vallist:
        tempnumlist = numlist.copy()
        for j in i:
            k = 0
            while k < len(tempnumlist):
                if tempnumlist[k] == j:
                    number01 = tempnumlist.pop(k - 1)
                    val = tempnumlist.pop(k - 1)
                    number02 = tempnumlist.pop(k - 1)

                    if val == "+":
                        tempnumlist.insert(k - 1, str(int(number01) + int(number02)))
                    elif val == "*":
                        tempnumlist.insert(k - 1, str(int(number01) * int(number02)))
                    else:
                        tempnumlist.insert(k - 1, str(int(number01) - int(number02)))
                else:
                    k += 1
        answer = max(answer, abs(int(tempnumlist[0])))

    return answer


expression = "100-200*300-500+20"
print(solution(expression))
