from collections import deque


def solution(x, y, n):
    global answer
    answer = float("inf")
    maxV = 1000000
    # dfs로 했다가 50점 ㅜ -> 시간초과

    def bfs(x, y):
        global answer
        queue = deque()
        queue.append([x, 0])  # 뒤에는 cnt
        visited = [False] * (maxV + 1)

        while queue:
            q, cnt = queue.popleft()
            if q > y or q > maxV or visited[q]:
                continue
            if q == y:
                answer = min(answer, cnt)
                continue
            visited[q] = True
            cnt += 1

            queue.append([q + n, cnt])
            queue.append([q*2, cnt])
            queue.append([q*3, cnt])

    bfs(x, y)
    if answer == float("inf"):
        answer = -1
    return answer
