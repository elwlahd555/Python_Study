N = int(input())

arr = [[0 for i in range(10)] for j in range(N + 1)]
for i in range(10):
    arr[1][i] = 1
for i in range(N + 1):
    arr[i][0] = 1

for i in range(2, N + 1):
    for j in range(1, 10):
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

print(sum(arr[N]) % 10007)
