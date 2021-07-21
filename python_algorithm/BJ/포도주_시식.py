n = int(input())
arr = [0] * (n+2)
for i in range(n):
    arr[i] = int(input())

dp = [0] * (n+2)
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], dp[1])
for i in range(3, n+2):
    dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3], dp[i - 1])

print(max(dp))
