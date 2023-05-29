def solution(want, number, discount):
    answer = 0
    # 10일 연속으로 일치할때 맞춰서 회원가입 하려고함.
    n = len(discount)
    for i in range(0, n-9):
        dis = discount[i:i+10]
        w = len(want)
        posible = True
        for j in range(w):
            if dis.count(want[j]) != number[j]:
                posible = False
        if posible:
            answer += 1
    return answer