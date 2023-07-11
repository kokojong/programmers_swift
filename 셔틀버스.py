def solution(n, t, m, timetable):
    timetable.sort()
    answer = 0
    l = len(timetable)

    def toInt(t):
        h, m = t.split(':')
        h, m = int(h), int(m)
        return h * 60 + m

    def toStr(t):
        h, m = t // 60, t % 60
        return str(h).zfill(2) + ":" + str(m).zfill(2)

    cnts = []  # 탄 사람들의 도착시간

    buses = []
    for i in range(n):
        buses.append(toInt('09:00') + t * i)
    # lastBus = buses[-1] # 막차시간
#     idx = 0 # 현재 idx
#     for bus in buses:
#         cnt = 0 # 해당 버스에 탄 사람들

#         while cnt < m and idx < l and bus >= toInt(timetable[idx]):
#             cnt += 1
#             idx += 1

#         if cnt < m: # 해당 버스에 자리가 있다면 타기
#             answer = bus
#         else: # 해당 버스에 자리가 없으면
#             answer = toInt(timetable[idx - 1]) - 1 # 제일 끝 사람보다 1분 빨리오기

#     return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)

    # 내가 다시 풀어본 방법
    # 각 버스마다 탄 사람들의 대기 시간을 배열로 만듬 (nts)
    for bus in buses:
        cnt = 0
        tmp = []
        while timetable and toInt(timetable[0]) <= bus and cnt < m:
            cnt += 1
            tmp.append(timetable.pop(0))

        cnts.append(tmp)

    c = cnts[-1]

    if len(c) == m:  # 가장 끝이 꽉찬경우
        answer = toInt(c[-1]) - 1
    # elif len(c) == 0: # 막차가 빈 경우 -> 막차 시간으로
    #     answer = buses[-1]
    else:  # 막차에 빈 공간이 있다면
        answer = buses[-1]
    # -> 묶어서 else 처리 가능

    return toStr(answer)
