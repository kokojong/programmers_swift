def solution(n, times):
    MAX = 10**9 * n
    answer = MAX

    left = 1
    right = MAX
    while left <= right:
        mid = (left + right) // 2

        cnt = 0  # 인원수
        for time in times:
            cnt += (mid // time)
        if cnt >= n:  # 가능하다면
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1

    return answer
