import math


def solution(N, road, K):
    answer = 0
    arr = [[math.inf for i in range(N + 1)] for j in range(N + 1)]

    for i in road:
        if arr[i[0]][i[1]] > i[2]:
            arr[i[0]][i[1]] = i[2]
            arr[i[1]][i[0]] = i[2]

    for i in range(N + 1):
        arr[i][i] = 0

    for path in range(N + 1):
        for i in range(N + 1):
            for j in range(N + 1):
                if arr[i][j] > arr[i][path] + arr[path][j]:
                    arr[i][j] = arr[i][path] + arr[path][j]

    for i in range(N + 1):
        if arr[1][i] <= K:
            answer += 1
    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3

print(solution(N, road, K))
