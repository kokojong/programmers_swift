import math


def solution(arrayA, arrayB):
    answer = 0

    gcdA = 0
    gcdB = 0
    for a in arrayA:
        gcdA = math.gcd(gcdA, a)
    for b in arrayB:
        gcdB = math.gcd(gcdB, b)

    # A로 arrayA를 나눌수 있는데 B는 안되는 경우 - gcdA
    isA = True
    for b in arrayB:
        if b % gcdA == 0:
            isA = False
    if isA:
        answer = max(answer, gcdA)

    # B로 arrayB를 나눌수 있는데 A는 안되는 경우 - gcdB
    isB = True
    for a in arrayA:
        if a % gcdB == 0:
            isB = False
    if isB:
        answer = max(answer, gcdB)

    return answer
