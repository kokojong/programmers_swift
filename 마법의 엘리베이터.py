import sys
sys.setrecursionlimit(10**7)


def solution(storey):
    answer = 0
    sto = list(str(storey))
    sto = list(map(int, sto))
    n = len(sto)
    results = []

    # 완탐으로 해보면 되지 않나? (storey가 짧다!, 가능한 경우의 수가 별로 없다!)

    def dfs(s, cnt):  # s: 기존 값, i: 10의 자리수
        # if len(str(s)) > n:
        #     result +=

        # global results
        m = s // 10  # 몫
        n = s % 10  # 나머지

        print("dfs", s, cnt, m, n)

        if m == 0:
            results.append(cnt + min(n, (10-n) % 10 + 1))
            # results.append(cnt + n)
            # results.append(cnt + (10-n)% 10 + 1 )
            # 남은수에서 자릿수가 올라가게 하고 처리하는것과 비교해서 더 작은거로
            # ex) 78 -> 8  요기서 8을 더해주는게 아니라 2를 더하고 10으로 만들어서 1번 더 빼주기로
            return

        # + 버튼
        c = (10-n)
        dfs(m+1, cnt + c)
        # - 버튼
        dfs(m, cnt + n)

    dfs(storey, 0)

    # print(results)

    answer = min(results)

    return answer
