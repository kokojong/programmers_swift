def solution(board, skills):
    answer = 0
    n = len(board)
    m = len(board[0])
    # for skill in skills:
    #     type, r1, c1, r2, c2, degree = skill
    #     # type 1 -> -, type 2 -> +
    #     for r in range(r1, r2+1):
    #         for c in range(c1, c2+1):
    #             if type == 1:
    #                 board[r][c] -= degree
    #             else:
    #                 board[r][c] += degree
    # 효율성 0점~
    # for r in range(n):
    #     for c in range(m):
    #         if board[r][c] > 0:
    #             answer += 1

    adds = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for skill in skills:
        type, r1, c1, r2, c2, degree = skill
        # type 1 -> -, type 2 -> +
        if type == 1:
            degree = (-1)*(degree)

        adds[r1][c1] += degree
        adds[r1][c2+1] -= degree
        adds[r2+1][c1] -= degree
        adds[r2+1][c2+1] += degree
    # print(adds)

    # adds의 누적합
    for r in range(n+1):  # 행의 누적합
        now = 0
        for c in range(m+1):
            now = now + adds[r][c]
            adds[r][c] = now

    for c in range(m+1):  # 열의 누적합
        now = 0
        for r in range(n+1):
            now = now + adds[r][c]
            adds[r][c] = now
    # print(adds)

    for r in range(n):
        for c in range(m):
            if board[r][c] + adds[r][c] > 0:
                answer += 1

    return answer
