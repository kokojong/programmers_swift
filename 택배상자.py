def solution(order):
    answer = 0
    n = len(order)
    # 보조 컨테이너: stack
    # 보조를 써도 안되면 더이상 싣지 않음 -> 끝
    stack = []
    idx = 0
    for i in range(1, n+1):
        stack.append(i)

        while len(stack) > 0 and stack[-1] == order[idx]:
            idx += 1
            stack.pop()
            answer += 1
        # print("stack", stack)

    return answer
