def solution(N, number):

    # N을 k번 이어붙인것: k-1 번 붙인거 +-*/ N, N그냥 이어붙인거 (dp?)
    # -> k번 이어붙인것: 1번 붙인거 + k-1번 붙인거 .... k-1번 붙인거 + 1번 붙인거

    dp = [set() for _ in range(9)]  # 0개로 만들수 있는건 빈것
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # i번만큼 이어붙인거

    for i in range(1, 9):
        for j in range(1, i):
            # print("i, j", i, j)
            for s1 in dp[j]:  # j가 더 작음
                for s2 in dp[i-j]:
                    # print("s1, s2", s1, s2)
                    dp[i].add(s1 + s2)
                    dp[i].add(s1 - s2)
                    dp[i].add(s1 * s2)
                    if s2 != 0:
                        dp[i].add(s1 / s2)

        if number in dp[i]:  # 체크
            return i
    return -1
