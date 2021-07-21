import re

def solution(str1, str2):
    listStr1 = {}
    listStr2 = {}
    for i in range(1, len(str1)):
        temp = (str1[i - 1] + str1[i]).lower()

        if len(re.findall("[a-zA-Z]", temp)) == 2:
            if temp in listStr1.keys():
                listStr1[temp] = listStr1.get(temp) + 1
            else:
                listStr1[temp] = 1

    for i in range(1, len(str2)):
        temp = (str2[i - 1] + str2[i]).lower()

        if len(re.findall("[a-zA-Z]", temp)) == 2:
            if temp in listStr2.keys():
                listStr2[temp] = listStr2.get(temp) + 1
            else:
                listStr2[temp] = 1
    lowlist = []
    maxlist = []
    maxdict = listStr2.copy()
    for i in listStr1.keys():
        if i in listStr2.keys():
            num = min(listStr1.get(i), listStr2.get(i))
            for j in range(num):
                lowlist.append(i)
        if i in listStr2.keys():
            maxdict[i] = max(listStr1.get(i), listStr2.get(i))
        else:
            maxdict[i] = listStr1.get(i)

    for i in maxdict.keys():
        for j in range(maxdict.get(i)):
            maxlist.append(i)

    if len(maxlist) == 0:
        return 65536
    else:
        return int(len(lowlist) / len(maxlist) * 65536)


str1 = "handshake"
str2 = "shake hands"

print(solution(str1, str2))
