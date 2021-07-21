def solution(s):
    answer = 0
    s_list = [i for i in s]

    for i in range(len(s_list)):
        s_list.append(s_list.pop(0))
        left_que = []
        cnt = len(s_list)
        for j in s_list:
            cnt -= 1
            if j == "[" or j == "(" or j == "{":
                left_que.append(j)

            elif j == "}":
                if len(left_que) == 0 or left_que.pop() != "{":
                    cnt = 10
                    break
            elif j == "]":
                if len(left_que) == 0 or left_que.pop() != "[":
                    cnt = 10
                    break
            elif j == ")":
                if len(left_que) == 0 or left_que.pop() != "(":
                    cnt = 10
                    break
        if cnt == 0 and len(left_que) == 0:
            answer += 1
    return answer


s = "[](){}"
print(solution(s))
