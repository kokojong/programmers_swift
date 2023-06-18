def solution(plans):
    answer = []  # 끝난 순서

    # 새로운 과제가 들어왔을 때 기존에 진행중인게 있다면 멈추고 새로운걸 시작, 배열(스택)에 넣음
    # 과제를 끝냈을때 그시간에 시작해야할 과제가 있다면 시작, 아니라면 배열에서 꺼냄
    # 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작합니다. -> Stack으로 확정

    arr = []  # plans
    stack = []  # 잠시 멈춘 과제들
    for plan in plans:
        name = plan[0]
        start = int(plan[1][:2]) * 60 + int(plan[1][3:])
        time = int(plan[2])
        # print(name, start, time)
        arr.append([name, start, time])
    arr.sort(key=lambda x: x[1])

    now = arr[0][1]  # 첫 과제의 시작시간
    n = 0  # 어떤 작업의 번호인지?

#     while n < len(arr):
#         stack.append(arr[n])
#         last = stack[-1]
#         if now < last[1]: # 현재 시간이 과제를 시작하는 시간 이전이라면
#             now = last[1] # 현재 시간을 바꿔줌

#         while stack and stack[-1][2] > 0: # 작업이 끝나지 않은게 있다면
#             # print("stack", stack)
#             now += 1
#             stack[-1][2] -= 1 # 과제의 남은양이 줄어듬

#             if stack[-1][2] == 0: # 그 과제가 끝나면
#                 answer.append(stack.pop()[0]) # answer에 이름 추가

#             if n + 1 < len(arr) and arr[n+1][1] == now: # 다음에 들어올 과제의 시작시간과 같다면
#                 # 현재 하던 과제를 그만두고 새로운 과제를 시작함
#                 n += 1
#                 stack.append(arr[n])

#         n += 1 # 이렇게 했는데도 시간이 남으면(잠시 멈춤 과제가 남아있지 않고 다음 과제를 시작하지 않았으면)

    while n < len(arr):
        stack.append(arr[n])

        if now < stack[-1][1]:
            now = stack[-1][1]

        while stack and stack[-1][2] > 0:  # 아직 끝나지 않은 과제가 있다면
            now += 1
            stack[-1][2] -= 1

            if stack[-1][2] == 0:
                answer.append(stack.pop()[0])

            if n + 1 < len(arr) and arr[n+1][1] == now:
                n += 1
                stack.append(arr[n])

        n += 1  # 밀린 과제 없으면 다음 과제 시작

    return answer
