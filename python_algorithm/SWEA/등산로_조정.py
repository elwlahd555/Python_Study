def solution():
    global visited, mx_cnt
    mx = 0
    for w in arr:
        mx = max(mx, int(max(w)))
    visited = [[False for k in range(N)] for k in range(N)]
    mx_cnt = 0
    for c in range(N):
        for j in range(N):
            if arr[c][j] == mx:
                visited[c][j] = True
                dfs(c, j, 1, False)
                visited[c][j] = False
    return mx_cnt


def dfs(x, y, cnt, dig):
    global visited, mx_cnt
    mx_cnt = max(mx_cnt, cnt)
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if cx < 0 or cy < 0 or cx >= N or cx >= N or visited[cx][cy] == True:
            continue
        visited[cx][cy] = True
        if arr[cx][cy] < arr[x][y]:
            dfs(cx, cy, cnt + 1, dig)
        else:
            if dig == False and K >= (1 + arr[cx][cy] - arr[x][y]):
                tmp = arr[cx][cy]
                arr[cx][cy] = arr[x][y] - 1
                dfs(cx, cy, cnt + 1, True)
                arr[cx][cy] = tmp
        visited[cx][cy] = False


T = int(input())

for t in range(T):
    temp = input().split(" ")
    global N, K, dx, dy, arr, visited, mx_cnt
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    N = int(temp[0])
    K = int(temp[1])
    answer = []
    arr = []

    for i in range(N):
        arr.append(input().split(" "))
    answer.append(solution())
    print(answer)
