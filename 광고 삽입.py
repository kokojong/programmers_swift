from collections import defaultdict


def timeToNum(time):
    h, m, s = time.split(':')
    return int(h)*3600 + int(m)*60 + int(s)


def numToTime(num):
    h = str(num//3600).zfill(2)
    m = str((num % 3600)//60).zfill(2)
    s = str(num % 60).zfill(2)

    return h+':'+m+':'+s


def solution(play_time, adv_time, logs):
    answer = 0
    # dict로 해서 초별로 저장하기..?
    dic = defaultdict(int)
    # 가장 많이 겹치는 부분을 가지고(근데 이제 앞 Index가 우선)
    # 슬라이딩 하면서 1분씩 이동하면 안되나?(누적합으로)

    play_time = timeToNum(play_time)
    adv_time = timeToNum(adv_time)

    partSum = 0
    starts = []  # 시작점들
    ends = []  # 끝점들

    dp = [0] * (play_time + 1)  # 0~playtime (0은 안씀)
    # 범위 0~play_time
    for l in logs:
        s1, s2 = l.split('-')
        t1 = timeToNum(s1)
        t2 = timeToNum(s2)
        # 직접 t1~t2로 하면 시간복잡도가 너무 높음 -> 시작점과 끝점만 따로 저장해보자
        dp[t1] += 1
        dp[t2] -= 1

    for i in range(1, play_time):
        dp[i] = dp[i] + dp[i-1]  # 구간 중간 채우기

    for i in range(1, play_time):
        dp[i] = dp[i] + dp[i-1]  # 누적합

    maxV = 0
    for i in range(adv_time - 1, play_time):  # end 지점
        v = dp[i] - dp[i - adv_time]
        if v > maxV:
            maxV = v
            answer = i - adv_time + 1

    return numToTime(answer)

    return numToTime(answer)
