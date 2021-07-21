def solution(rows, columns, queries):
    answer = []
    arr = [[0 for i in range(columns + 1)] for j in range(rows + 1)]
    cnt = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i][j] = cnt
            cnt += 1
    for t in queries:
        low_num = rows * columns
        prev_num = arr[t[0]][t[1]]
        low_num = min(low_num, prev_num)
        for i in range(t[1] + 1, t[3] + 1):
            temp_num = arr[t[0]][i]
            arr[t[0]][i] = prev_num
            prev_num = temp_num
            low_num = min(low_num, prev_num)
        for i in range(t[0] + 1, t[2] + 1):
            temp_num = arr[i][t[3]]
            arr[i][t[3]] = prev_num
            prev_num = temp_num
            low_num = min(low_num, prev_num)
        for i in range(t[3] - 1, t[1] - 1, -1):
            temp_num = arr[t[2]][i]
            arr[t[2]][i] = prev_num
            prev_num = temp_num
            low_num = min(low_num, prev_num)
        for i in range(t[2] - 1, t[0] - 1, -1):
            temp_num = arr[i][t[1]]
            arr[i][t[1]] = prev_num
            prev_num = temp_num
            low_num = min(low_num, prev_num)
        answer.append(low_num)
    return answer


rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))
