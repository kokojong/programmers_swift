def solution(sequence):
    answer = 0
    n = len(sequence)
    dp1 = []
    dp2 = []
    # idea: 새로운게 더해질때는 그전까지  -1 +1 로 진행되다가 이번에 -1 를 하는것
    # 또는 +1 -1 로 진행되다가 이번에는 +1을 하는것

    s1 = []
    s2 = []

    for i in range(n):
        s1.append(sequence[i] * (-1)**(i+1))
        s2.append(sequence[i] * (-1)**(i+2))

    dp1.append(s1[0])
    dp2.append(s2[0])
    for i in range(1, n):
        dp1.append(max(0, dp1[i-1]) + s1[i])
        dp2.append(max(0, dp2[i-1]) + s2[i])

    answer = max(max(dp1), max(dp2))

    return answer
