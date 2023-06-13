def solution(maps):
    answer = -1

    r = len(maps)
    c = len(maps[0])

    for i in range(r):
        for j in range(c):
            m = maps[i][j]
            if m == "S":
                start = (i, j)
            if m == "L":
                lever = (i, j)
            if m == "E":
                end = (i, j)

    def bfs(now, target, cnt):
        visited = [[False for _ in range(c)] for _ in range(r)]
        queue = []
        queue.append((now[0], now[1], 0))

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while queue:
            qr, qc, cost = queue.pop(0)
            if visited[qr][qc]:
                continue
            visited[qr][qc] = True
            if (qr, qc) == target:
                return cost

            for i in range(4):
                rr = qr + dr[i]
                cc = qc + dc[i]

                if 0 <= rr < r and 0 <= cc < c and (visited[rr][cc] == False) and maps[rr][cc] != "X":
                    queue.append((rr, cc, cost + 1))

        return -1  # 불가능

    toLever = bfs(start, lever, 0)
    toEnd = bfs(lever, end, 0)

    if toLever != -1 and toEnd != -1:
        answer = toLever + toEnd

    return answer
