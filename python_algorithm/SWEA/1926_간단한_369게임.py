N = int(input())

# 1부터 N까지
for i in range(1, N + 1):
    # 결과를 담아줄 ans
    ans = ""
    # 해달하는 숫자에 3,6,9가 있다면
    if "3" in str(i) or "6" in str(i) or "9" in str(i):
        for j in str(i):
            if "3" in j or "6" in j or "9" in j:
                ans += "-"
    else:
        ans = str(i)
    print(ans, end=" ")
