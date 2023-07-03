from collections import defaultdict


def solution(tickets):
    answer = []

    dic = defaultdict(list)
    for ticket in tickets:
        tmp = dic[ticket[0]]
        tmp.append(ticket[1])
        dic[ticket[0]] = tmp

    for k, v in dic.items():
        v.sort(reverse=True)  # pop(0) 대신 pop()을 하기 위함

    stack = []
    stack.append("ICN")

    while stack:
        s = stack[-1]

        if dic[s]:  # s로 시작하는 애들이 남아있다면
            stack.append(dic[s].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]
