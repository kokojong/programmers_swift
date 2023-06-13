def solution(book_time):
    answer = 0
    times = []
    for time in book_time:
        start = time[0]
        h1 = int(start[:2])
        m1 = int(start[3:])
        end = time[1]
        h2 = int(end[:2])
        m2 = int(end[3:]) + 10  # 끝나고 10분간 청소해야함
        times.append([h1 * 60 + m1, h2 * 60 + m2])

    times.sort(key=lambda x: (x[0], x[1]))  # 시작 시간, 끝시간 우선순위로 정렬
    minTime = 24 * 60  # 24:00
    maxTime = 0  # 00:00

    for time in times:
        minTime = min(minTime, time[0])
        maxTime = max(maxTime, time[1])

    for i in range(minTime, maxTime+1):  # 각 초를 지나면서 몇개가 필요한지 체크?
        cnt = 0
        for time in times:
            if time[0] <= i < time[1]:
                cnt += 1
        # print(i, cnt)
        answer = max(answer, cnt)

    # stacks = [] # room별 끝나는 시간

#     for time in times:
#         s = time[0]
#         e = time[1]

#         if stacks:

#         else:
#             stacks.append(e) # 끝나는 시간을 하나 넣음
#         answer = max(answer, len(stacks)) # 동시에 가장 많은 시간대 찾기

    return answer
