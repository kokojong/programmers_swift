def solution(maps):
    answer = []
    r = len(maps)
    c = len(maps[0])

    arr = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maps[i][j] != "X":
                arr[i][j] = int(maps[i][j])

    for i in range(r):
        for j in range(c):

            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]

            queue = []
            cnt = 0

            if arr[i][j]:
                queue.append([i, j])

            while queue:
                # print("queue", queue)
                ii, jj = queue.pop(0)

                if arr[ii][jj]:
                    # visited[ii][jj] = True
                    cnt += arr[ii][jj]
                    arr[ii][jj] = 0  # 0으로 초기화

                    for d in range(4):
                        rr = dr[d] + ii
                        cc = dc[d] + jj
                        if 0 <= rr < r and 0 <= cc < c and arr[rr][cc]:
                            queue.append([rr, cc])
            if cnt > 0:
                answer.append(cnt)
    answer.sort()
    if not answer:  # 비면 -1
        answer.append(-1)
    return answer
