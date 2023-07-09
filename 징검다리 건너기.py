def solution(stones, k):
    answer = 0
    maxV = max(stones)

    left = 0
    right = maxV

    while left <= right:
        mid = (left + right) // 2  # mid명
        # print("l m r", left, mid ,right)

        jump = 0  # 몇칸이나 건너뛰었는지 -> 애가 k보다 커지면 false
        for stone in stones:
            if jump < k:  # 아직 가능함
                if stone - mid > 0:  # m명이 지나갔어도 가능
                    jump = 0  # 그냥 건널수 있다면 far 초기화
                else:
                    jump += 1  # 쩜프하면
            else:
                break

        if jump < k:  # mid명이 건너는게 가능하다면 -> 더 많은 사람으로 해보기
            left = mid + 1
        else:  # mid명이 건너는게 불가능하다면 -> 더 적은 사람으로 해보기
            right = mid - 1
            answer = mid

    return answer
