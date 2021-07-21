def solution(m, n, board):
    boards = [[i for i in j] for j in board]

    cnt = 10
    while cnt != 0:
        cnt = 0
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if boards[i][j] != 0 and boards[i][j] == boards[i][j + 1] == boards[i + 1][j] == boards[i + 1][j + 1]:
                    visited[i][j] = True
                    visited[i + 1][j] = True
                    visited[i][j + 1] = True
                    visited[i + 1][j + 1] = True
                    cnt += 1
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    for k in range(i, -1, -1):
                        if k == 0:
                            boards[k][j] = 0
                        else:
                            boards[k][j] = boards[k - 1][j]
    answer = 0
    for i in boards:
        for j in i:
            if j == 0:
                answer += 1
    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))
