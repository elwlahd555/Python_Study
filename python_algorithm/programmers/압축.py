import re


def solution(msg):
    answer = []
    msglist = re.findall("[a-z]", msg.lower())
    dictlist = [0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]

    while len(msglist) != 0:
        breaker = False
        for i in range(len(msglist), 0, -1):
            temp = "".join(msglist)[:i]
            if temp in dictlist:
                for j in range(len(dictlist)):
                    if dictlist[j] == temp:
                        answer.append(j)
                        dictlist.append("".join(msglist)[:i + 1])
                        while i > 0:
                            msglist.pop(0)
                            i -= 1
                        breaker = True
                        break
            if breaker:
                break
    return answer


msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))
