def solution(n, money):
    answer = 0
    money.sort()
    dp = [0] * (n+1)
    dp[0] = 1  # dp[5-5] = 1로 해서 추가해야함

    for m in money:
        # 작은 m부터 보면서 dp를 수정해줌
        for i in range(1, n + 1):
            if i >= m:  # m보다 크거나 같을 때(m을 사용할 수 있을 때)
                dp[i] = dp[i] + dp[i - m]
    answer = dp[-1] % 1000000007
    return answer
