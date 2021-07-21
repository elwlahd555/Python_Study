def solution(s):
    cnt = 0
    zero_cnt = 0
    while s != "1":
        temp_s = ""
        for i in s:
            if i == "1":
                temp_s += i
            else:
                zero_cnt += 1
        s = format(len(temp_s), 'b')
        cnt += 1
    answer = [cnt, zero_cnt]
    return answer


s = "110010101001"
print(solution(s))
