import math


def solution(n, stations, w):
    answer = 0

    # 시간초과 나고 대충의 풀이는 생각했는데 아쉽스 ㅜㅜ
    s = 1
    for station in stations:
        e = station - w - 1  # 닿지 않는 부분의 end(예제 1의 경우 2)
        # print(s, e)
        answer += math.ceil((e - s + 1) / (2*w+1))
        s = station + w + 1

    if e < n:  # 끝이 안난경우
        answer += math.ceil((n - s + 1) / (2*w + 1))

    return answer

    # 말만 이진탐색 ㅋㅋㅋ(시간초과 ㅜ)

    # 이진탐색
    # l = 0
    # r = n-1
#     visited = [False] * n
#     for station in stations:
#         # station - w, station, station + w
#         if station -1 -w >= 0:
#             start = station - w -1
#         else:
#             start = 0

#         if station -1 + w <= n-1:
#             end = station + w -1
#         else:
#             end = n-1

#         for i in range(start, end+1):
#             visited[i] = True

#     def checkIsPosible(k, visited): # k개로 가능한지 판단
#         cnt = 0 # 최소한의 갯수
#         for i in range(n):
#             if visited[i] == False:
#                 start = i
#                 end = i + 2*w
#                 if end > n-1:
#                     end = n-1
#                 for j in range(start, end+1):
#                     visited[j] = True
#                 cnt += 1

#         if k >= cnt: # k개로 가능함
#             return True
#         else:
#             return False

#     while l <= r:
#         mid = (l + r) // 2
#         # print(l, mid, r)

#         # mid개로 도전해봄
#         checkIsPosible(mid, copy.deepcopy(visited))
#         # print("posible", posible)
#         if posible:
#             r = mid - 1 # 더 적은 갯수로 도전
#             answer = min(answer, mid)
#         else:
#             l = mid + 1 # 더 많은 갯수로 도전

#     return answer
