def solution(s):
    answer = 1

    n = len(s)

#     for i in range(n, 0, -1): # 부분 문자열의 길이
#         for j in range(0, n - i + 1):
#             ss = s[j:j+i]
#             # kk = "".join(list(reversed(ss)))
#             kk = ss[::-1]
#             if ss == kk:
#                 return i

#             # m = len(ss)
#             # isPosible = True
#             # for k in range(m):
#             #     # print(ss, ss[k], ss[m-k-1])
#             #     if ss[k] != ss[m-k-1]:
#             #         isPosible = False
#             #         break
#             # if isPosible:
#             #     return i
#     return answer

    # dp 풀이
    dp = [[0 for _ in range(n)] for _ in range(n)]  # [start][end]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = dp[i][i]+1  # 2개가 붙어있는 경우

    for i in range(n):
        for j in range(i, n):
            k = 1
            while dp[i][j] and i >= k and j <= n - k - 1 and s[i-k] == s[j+k]:
                # if s[i-k] == s[j+k]:
                dp[i-k][j+k] = dp[i][j] + k*2
                answer = max(answer, dp[i-k][j+k])
                k += 1

    # print(dp)

    return answer
