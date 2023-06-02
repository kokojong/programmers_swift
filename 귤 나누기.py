from collections import Counter


def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    arr = []
    for i in counter:
        c = counter[i]  # 몇개인지
        arr.append(c)

    arr.sort()

    while k > 0:
        k -= arr.pop()  # 많은것 부터 없앰
        answer += 1

    return answer
