from collections import deque


def solution(board):
    answer = [0]
    dq = deque()
    n = len(board)

    dr = [-1, 0, 1, 0]  # U R D L 순 0, 1, 2, 3
    dc = [0, 1, 0, -1]

    visited = [[[10**9 for _ in range(4)] for c in range(n)] for _ in range(n)]
    # cost, r ,c

    for i in range(4):
        visited[0][0][i] = 0  # 다 방문처리 및 cost 0원

    if board[0][1] == 0:
        visited[0][1][2] = 100
        dq.append([0, 1, 100, 1])  # r, c, cost, direction(R = 1)

    if board[1][0] == 0:
        visited[1][0][2] = 100
        dq.append([1, 0, 100, 2])  # r, c, cost, direction(D = 2)

    while dq:
        qr, qc, cost, direc = dq.popleft()  # r, c, direction
        # print(qr, qc, cost, direc)
        for i in range(4):
            rr = qr + dr[i]
            cc = qc + dc[i]

            if direc != i:  # 이전과 같지 않으면
                new_cost = cost + 600
            else:
                new_cost = cost + 100
            # print("cost", cost)
            if 0 <= rr < n and 0 <= cc < n and board[rr][cc] == 0:
                if visited[rr][cc][i] > new_cost:  # 더 적은 값으로 가능하다면
                    visited[rr][cc][i] = new_cost
                    dq.append([rr, cc, new_cost, i])

    # print(visited[n-1][n-1])
    answer = min(visited[n-1][n-1])

    return answer
