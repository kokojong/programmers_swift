from collections import Counter


def solution(weights):
    answer = 0
    # 거리: 2 3 4
    # 가능한 비율: 1:1, 2:3, 1:2, 3:4
    c = dict(Counter(weights))

    for k, v in c.items():
        # print("k, v", k, v)
        # 1:1
        if v > 1:  # 같은 무게인 사람들 v C 2 (2개 선택) -> v*(v-1) / 2
            answer += v * (v-1) / 2
        # 2:3
        if c.get(k*3/2):
            answer += v * c[k*3/2]
        # 1:2
        if c.get(k*2):
            answer += v * c[k*2]
        # 3:4
        if c.get(k*4/3):
            answer += v * c[k*4/3]

    return answer
