from heapq import heappush, heappop


def solution(n, k, enemy):
    hq = []
    e = len(enemy)

    # for round, monster in enumerate(enemy):
    #     heappush(hq, monster)
    #     print(round)
    #     if len(hq) > k:
    #         n -= heappop(hq)
    #     if n < 0:
    #         return round

    for i in range(e):
        heappush(hq, enemy[i])
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return i

    return e
