from collections import Counter


def solution(topping):
    answer = 0
    # 잘린 조각들의 크기와 올려진 토핑의 개수에 상관없이 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 롤케이크가 나누어진 것으로 생각합니다.

    # 처음에 아래와 같이 했는데 시간초과 발생(100만개라서 O(n) 으로 하면 틀림)
    # for i in range(1, n):
    #     left = topping[:i]
    #     right = topping[i:]
    #     if len(set(left)) == len(set(right)):
    #         answer += 1

    n = len(topping)
    # bro = Counter(topping)
    bro = {}  # Counter 대신 단순하게 dict로 구성한 방법
    for t in topping:
        if t in bro:
            bro[t] += 1
        else:
            bro[t] = 1
    # print(bro) # Counter({1: 4, 2: 2, 3: 1, 4: 1})
    me = set()
    for i in topping:
        bro[i] -= 1  # 그만큼 내가 가져감
        if bro[i] == 0:
            del bro[i]  # 아예 없는 딕셔너리가 된다.

        me.add(i)  # 내가 가진 토핑 -> set이라서 add 해주면 된다.
        if len(me) == len(bro):
            answer += 1

    return answer
