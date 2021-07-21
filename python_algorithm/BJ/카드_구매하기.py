N = int(input())
card = [0]
card += list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = card[1]
for i in range(2, N + 1):
    dp[i] = card[i]
    for j in range(1, i // 2 + 1):
        if dp[i] < dp[i - j] + dp[j]:
            dp[i] = dp[i - j] + dp[j]

print(dp[N])
