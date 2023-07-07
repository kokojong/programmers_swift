from collections import defaultdict


def solution(gems):
    answer = []
    n = len(gems)
    jew = len(set(gems))  # 보석의 가짓수

    # 투포인터?
    # start = 0

    # while start <= end:

    # start를 하나씩 올려가면서 체크하기
    # 이유: 시작하는 점을 바꿔주면서 그 자리에서 가장 빠르게 조건을 만족하는걸 찾기

    # 시간초과 (너무 많은 것들이 될때)
#     minL = 10**6
#     for start in range(n):
#         end = 0

#         while end < n:
#             part = gems[start:end+1]
#             if len(set(part)) == jew:
#                 # print("part", part)
#                 if len(part) < minL: # 이 길이가 최소 길이 보다 작을때만 갱신
#                     minL = len(part)
#                     answer = [start+1, end+1]
#                     # result.append([start+1, end+1, len(part)]) # 시작점, 끝점, 길이
#                 break
#             else:
#                 end += 1
    # result = sorted(result, key = lambda x: x[2])[0]
    # answer = result[:2] # 길이는 잘라내기

    # 다시~
    start = 0
    end = 0
    minL = 10**6

    # tmp = [gems[0]]
    dic = defaultdict(int)
    dic[gems[0]] += 1

    while start <= end and end < n:
        # print("tmp", tmp)
        if len(dic) == jew:
            # print("만족", dic, len(dic))
            # l = 0 # 모든 딕셔너리 값의 합
            l = end - start + 1
            # for d in dic.values() :
            #     l += d
            if l < minL:
                minL = l
                # print("작은경우", start, end, minL)
                answer = [start+1, end+1]

            # tmp.pop(0)
            dic[gems[start]] -= 1
            if dic[gems[start]] <= 0:
                # print("del")
                del(dic[gems[start]])
            start += 1

        else:
            end += 1
            # print("start, end", start ,end)
            if end < n:
                dic[gems[end]] += 1
                # tmp.append(gems[end])

    return answer
