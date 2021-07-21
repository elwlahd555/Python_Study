n, k = [int(i) for i in input().split(" ")]
num = []
result = [0 for i in range(k + 1)]
result[0] = 1
for i in range(n):
    num.append(int(input()))

for i in num:
    for j in range(i, k + 1):
        if j - i >= 0:
            result[j] += result[j - i]

print(result[k])
