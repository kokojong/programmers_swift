def solution(board):
    global answer
    answer = 1  # 가능 - 1, 불가능 0
    # 선공이 O, 후공이 X
    # 순서를 헷갈린 경우
    # 이미 승리했는데 계속 진행한 경우

    def checkOrder(board):
        global answer
        cntO = 0
        cntX = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    cntO += 1
                elif board[i][j] == 'X':
                    cntX += 1
        return (cntO, cntX)

    def checkWin(board):
        winO = False
        winX = False

        # 가로 체크
        for i in range(3):
            if board[i] == "OOO":
                winO = True
            if board[i] == "XXX":
                winX = True
        # 세로 체크
        for j in range(3):
            result = True
            v = board[0][j]
            for i in range(1, 3):
                if board[i][j] != v:
                    result = False
            if result:
                if v == "O":
                    winO = True
                elif v == "X":
                    winX = True

        # 대각선 체크
        cross1 = board[0][0] + board[1][1] + board[2][2]
        cross2 = board[2][0] + board[1][1] + board[0][2]
        # print("cross", cross1, cross2)
        if cross1 == "OOO" or cross2 == "OOO":
            winO = True
        if cross1 == "XXX" or cross2 == "XXX":
            winX = True

        return (winO, winX)

    o, x = checkOrder(board)
    if o < x or abs(o - x) > 1:  # 후공이 더 많거나 둘의 차이가 2개이상인 경우
        answer = 0  # 실패

    # 승리 체크
    oo, xx = checkWin(board)
    # print("oo, xx", oo, xx)

    # 선공에서 게임이 끝났는데 후공을 둔 경우 (둘이 똑같을때)
    if o == x and oo:  # 이미 선공이 이김
        answer = 0

    # 후공에서 게임이 끝났는데 선공을 둔 경우(o > x일때)
    elif o > x and xx:
        answer = 0

    return answer
