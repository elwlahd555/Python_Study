def find(place):
    result = 1
    search = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                que = [[i, j]]
                visited = [[False for i in range(5)] for j in range(5)]
                visited[i][j] = True
                cnt = 0
                while len(que) != 0 and cnt < 2:
                    size = len(que)
                    for a in range(size):
                        p = que.pop(0)
                        for k in search:
                            x = p[0] + k[0]
                            y = p[1] + k[1]
                            if 0 <= x < 5 and 0 <= y < 5 and not visited[x][y]:
                                if place[x][y] == "P":
                                    return 0
                                elif place[x][y] == "O":
                                    que.append([x, y])
                                    visited[x][y] = True
                                else:
                                    visited[x][y] = True
                    cnt += 1
    return result


def solution(places):
    answer = []
    for i in range(5):
        place = []
        for j in range(5):
            place.append(list(places[i][j]))
        answer.append(find(place))

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
