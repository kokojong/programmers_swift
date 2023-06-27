import heapq


def solution(jobs):
    jobs.sort()
    answer = 0
    i = 0
    h = []
    n = len(jobs)

    start_total = 0
    end_total = 0
    end = 0
    now = 0

    while jobs or h:  # 남은 할일 or heap이 남아있다면
        while jobs:
            if now >= jobs[0][0]:  # 제일 먼저 들어온 거부터 확인 -> now 이하이면 heap에 삽입
                s, time = jobs.pop(0)  # 들어온 시간, 소요시간
                start_total += s
                heapq.heappush(h, [time, s])
            else:
                break  # 스케줄링 end타임

        if h:
            e, _ = heapq.heappop(h)
            now += e  # 실행 시간만큼 end가 바뀜
            end_total += now
        else:
            now = jobs[0][0]  # 비어있을 때?
    answer = int((end_total - start_total) / n)
    return answer


#     start, end = -1, 0

#     while i < len(jobs):
#         for job in jobs[i:]:
#             if start < job[0] <= end: # 아직 안끝났으면 -> heapq에 넣어줌
#                 heapq.heappush(h, [job[1], job[0]])

#         if len(h) > 0:
#             p = heapq.heappop(h)
#             start = end
#             end += p[0] # 실행 시간만큼 end가 늘어남
#             answer += (end - p[1]) # 끝난 시간 - 시작시간
#             i += 1
#         else:
#             end += 1


#     return int(answer/len(jobs))
