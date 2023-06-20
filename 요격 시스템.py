def solution(targets):
    targets.sort()  # 시작하는 지점 기준으로 정렬
    answer = 0
    end = 0

    for target in targets:
        # print(target, end)
        if target[0] >= end:  # 끝점보다 뒤 -> 무조건 새로운거로 시작
            end = target[1]
            answer += 1
        elif target[0] < end:  # 범위내라면
            end = min(end, target[1])  # 더 작은걸 end로 지정

    return answer
