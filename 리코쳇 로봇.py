def solution(board):
    global answer
    answer = -1
    r, c = len(board), len(board[0])

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                start = (i, j)
            if board[i][j] == 'G':
                end = (i, j)

    def bfs(board, start, end, cnt):
        global answer
        visited = [[-1 for _ in range(c)] for _ in range(r)]
        queue = []
        queue.append((start[0], start[1], cnt))
        visited[start[0]][start[1]] = 0

        while queue:
            qr, qc, cost = queue.pop(0)
            if (qr, qc) == end:
                answer = cost
                # print("Goal", cost)
                return
            # print("q is", (qr, qc, cost))

            cost += 1
            # 위
            for y in range(qr, -1, -1):
                if board[y][qc] == "D":
                    rr = y + 1  # 해당 위치가 벽이면 그 위를 고름
                    break
                elif y == 0:
                    rr = y  # 끝점인 경우
                    break
            # print("rr up", rr)
            if visited[rr][qc] == -1:
                visited[rr][qc] = cost
                queue.append((rr, qc, cost))

            # 왼쪽
            for x in range(qc, -1, -1):
                if board[qr][x] == "D":
                    cc = x + 1  # 해당 위치가 벽이면 그 오른쪽을 고름
                    break
                elif x == 0:
                    cc = x  # 끝점인 경우
                    break
            # print("cc left", cc)
            if visited[qr][cc] == -1:
                visited[qr][cc] = cost
                queue.append((qr, cc, cost))

            # 아래
            for y in range(qr, r):
                if board[y][qc] == "D":
                    rr = y-1  # 해당 위치가 벽이면 그 위를 고름
                    break
                elif y == r-1:
                    rr = y  # 끝점인 경우
                    break
            # print("rr down", rr, visited[rr][qc])
            if visited[rr][qc] == -1:
                visited[rr][qc] = cost
                queue.append((rr, qc, cost))

            # 오른쪽
            for x in range(qc, c):
                if board[qr][x] == "D":
                    cc = x - 1  # 해당 위치가 벽이면 그 왼쪽을 고름
                    break
                elif x == c-1:
                    cc = x  # 끝점인 경우
                    break
            # print("cc left", cc)
            if visited[qr][cc] == -1:
                visited[qr][cc] = cost
                queue.append((qr, cc, cost))

    bfs(board, start, end, 0)

    return answer
