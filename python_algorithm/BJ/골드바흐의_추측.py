T = int(input())

num = [0 for i in range(10001)]
num[0] = 1
num[1] = 1

for i in range(2, 10001):
    if num[i] == 0:
        temp = i
        k = 2
        for j in range(2, 10001):
            if temp * j > 10000:
                break
            num[temp * j] = 1

for i in range(T):
    k = int(input())
    for j in range(k // 2, k):
        if num[j] == 0 and num[k - j] == 0:
            print(f"{k - j} {j}")
            break
