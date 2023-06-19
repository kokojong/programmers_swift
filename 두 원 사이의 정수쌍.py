import math


def solution(r1, r2):
    answer = 0
    # x**2 + y**2 = r**2
    # y = (r**2 - x**2) ** (1/2)

    for x in range(1, r2+1):
        y2 = math.sqrt(r2**2 - x**2)

        if (r1**2 - x**2) >= 0:
            y1 = math.sqrt(r1**2 - x**2)
        else:
            y1 = 0
        # print(math.floor(y2), math.ceil(y1))
        answer += math.floor(y2) - math.ceil(y1) + 1
    return answer * 4
