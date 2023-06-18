def solution(picks, minerals):
    answer = 0
    # 무조건 5개씩 캐야함
    # minerals의 길이는 50이하 -> 최대 곡괭이는 10개만 사용하게 된다.
    # 다이아 곡괭이가 가장 피로도를 적게 쓰니까 제일 합(?) 이 큰애부터 다이아로 쓰기

    diaPick, ironPick, stonePick = picks[0], picks[1], picks[2]
    totalPicks = diaPick + ironPick + stonePick

    arr = []  # 5개씩 나눈 배열 (cost, dia, iron, stone)
    while minerals and totalPicks:
        group = minerals[:5]
        d, i, s = 0, 0, 0
        for g in group:
            if g == 'diamond':
                d += 1
            elif g == 'iron':
                i += 1
            elif g == 'stone':
                s += 1
        tmp = (d*25 + i*5 + s, d, i, s)
        arr.append(tmp)
        minerals = minerals[5:]
        totalPicks -= 1

    arr.sort(key=lambda x: x[0], reverse=True)
    # print(arr)

    while arr:
        totalPick = diaPick + ironPick + stonePick
        q = arr.pop(0)
        if diaPick:
            answer += q[1] + q[2] + q[3]
            diaPick -= 1
        elif ironPick:
            answer += q[1] * 5 + q[2] + q[3]
            ironPick -= 1
        elif stonePick:
            answer += q[1] * 25 + q[2] * 5 + q[3]
            stonePick -= 1

    return answer
