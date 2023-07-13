import copy


def solution(key, lock):
    # 최대 크기는 N*N이 9개 있는 경우(3N * 3N)
    m = len(key)
    n = len(lock)

    def turnKey():
        tmp = [[-1 for _ in range(m)] for _ in range(m)]
        for r in range(m):
            for c in range(m):
                tmp[c][m - r - 1] = key[r][c]
        return tmp

    def setKey(i, j):  # 보드의 i, j에 key를 올려놓기(겹쳐서)
        newBoard = copy.deepcopy(board)  # 3n * 3n 중간에 lock이 올려진거

        for r in range(i, i+m):  # key의 크기만큼 올려두는거니까 맞음
            for c in range(j, j+m):  # i, j 에 올려두기
                # r,c는 board에서의 위치
                # i~i+m-1, j~j+m-1
                if newBoard[r][c] == -1:  # 아무것도 없던 경우
                    newBoard[r][c] = key[r-i][c-j]
                else:
                    if newBoard[r][c] == key[r-i][c-j]:  # key와 Lock이 같은 모양인 경우 -> 틀림
                        return False
                    else:  # 둘이 다르면 - 합쳐주기
                        newBoard[r][c] = newBoard[r][c] + key[r-i][c-j]

        # n,n ~ 2n-1, 2n-1까지 검사
        for r in range(n, 2*n):
            for c in range(n, 2*n):
                if newBoard[r][c] != 1:  # 1이 아니라면
                    return False
        return True

    # 0~3n-1
    board = [[-1 for _ in range(3*n)] for _ in range(3*n)]
    # 중간에 Lock을 올려둠 (n~2n-1 까지)
    for i in range(n):
        for j in range(n):
            board[i+n][j+n] = lock[i][j]

    # 시작점 -> 0,0 ~ 2n-1, 2n-1 까지 key를 올려둬보기(key의 시작점)
    for _ in range(4):  # 키를 4번 돌려보기
        key = turnKey()
        for i in range(1, 2*n):
            for j in range(1, 2*n):
                if setKey(i, j):  # key를 놓는 시작점 (0, 3*n - m)
                    return True

    return False
