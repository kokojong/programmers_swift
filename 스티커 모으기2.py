def solution(sticker):
    answer = 0
    n = len(sticker)

    if n <= 3:
        return max(sticker)

    dp1 = [0] * n
    dp1[0] = sticker[0]  # 처음것 뽑을수 있음
    dp1[1] = dp1[0]  # 0번을 뽑아서 1번은 못뽑음 -> 0번과 동일

    for i in range(2, n-1):  # n-1번은 못뽑음
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    # print(dp1)

    dp2 = [0] * n
    dp2[1] = sticker[1]  # 처음것 안뽑음, 1번은 뽑음

    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    # print(dp2)

    answer = max(max(dp1), max(dp2))
    return answer
