from itertools import permutations
def solution(k, dungeons):
    answer = -1
    # 던전의 갯수는 1~8개 -> 완탐 가능
    n = len(dungeons)

    for i in range(1, n+1): # i: 몇개 선택했는지
        for per in permutations(list(range(n)) , i):
            energy = k
            posible = True
            # print(per)
            for p in per:
                least, cost = dungeons[p][0], dungeons[p][1]
                # print(energy, p, least, cost)
                if energy >= least:
                    energy -= cost
                else:
                    posible = False
            if posible:
                answer = max(answer, i)
            # print(posible)
    return answer