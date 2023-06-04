def solution(k, d):
    answer = 0
    # d,0  d-1,1 ..... 1,d-1  0, d

    # n = d//k # 나눈 값
    # answer = (n+1)**2 - (n+1)*n// 2
    # answer = (n+1)**2
    # for i in range(n+1): # 0~n
    #     for j in range(n+1):
    #         k =  (i**2 + j**2)**(1/2)
    #         # print(i, j, k)
    #         if k <= n:
    #             answer += 1

    for i in range(0, d+1, k):
        y = (d**2 - i**2)**(1/2)
        answer += int(y/k) + 1  # y까지를 k로 나눈거 + 0도 있어서 1개 추가
    return answer
