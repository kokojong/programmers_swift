def solution(numbers):
    n = len(numbers)
    answer = []
    stack = []

    # 끝에서부터 오면서 stack으로 처리
#     for i in range(n):
#         j = n - i -1

#         # stack에서 제일 위에가 나보다 크다면 answer에 stack[-1]해줌
#         if stack:

#         else:

    # 20~23번 시간초과
#     for i in range(n):
#         now = numbers[i]

#         for j in range(i+1, n):
#             if numbers[j] > now:
#                 answer[i] = numbers[j]
#                 break

#     for r in reversed(numbers):
#         while stack:
#             # print("ss", stack)
#             last = stack[-1]
#             if last > r:
#                 answer.append(last)
#                 stack.append(r)
#                 break
#             else:
#                 stack.pop()

#         if not stack:
#             stack.append(r)
#             answer.append(-1)
#             # print("s", stack)
#     answer.reverse()

    for r in reversed(numbers):
        while stack:
            last = stack[-1]
            # 마지막거보다 작을때까지 pop하고 r을 스택에 추가(다음을 위해), answer에는 last값 추가
            if r < last:
                answer.append(last)
                stack.append(r)
                break  # while 종료
            else:
                stack.pop()

        if not stack:
            stack.append(r)
            answer.append(-1)

    answer.reverse()
    # 누군가의 답안
#     answer = [-1] * len(numbers)
#     stack = []

#     for idx, number in enumerate(numbers):
#         while stack and numbers[stack[-1]] < number:
#             answer[stack.pop()] = number

#         stack.append(idx)

    return answer
