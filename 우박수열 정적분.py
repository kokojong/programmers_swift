def solution(k, ranges):
    answer = []
    dots = []
    x = 0
    y = k
    while y != 1:
        dots.append([x, y])
        if y % 2 == 0:
            y = y//2
        else:
            y = y*3 + 1
        x += 1
    dots.append([x, y])

    areas = []  # 각 영역별 크기
    for i in range(x):
        l = dots[i]
        r = dots[i+1]
        area = min(l[1], r[1]) + abs(r[1] - l[1])/2
        areas.append(area)

    for rang in ranges:
        l = rang[0]  # 시작점
        r = x + rang[1]

        if r < l:
            answer.append(-1.0)
        elif r == l:
            answer.append(0.0)
        else:
            answer.append(sum(areas[l:r]))
    return answer
