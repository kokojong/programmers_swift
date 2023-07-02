from collections import deque


def solution(begin, target, words):
    answer = 0

    def check(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        return cnt == 1  # 둘이 한 글자만 다르다면 True

    queue = deque()
    visited = []

    queue.append((begin, 0))

    while queue:
        # print("queue", queue)
        # print("visited", visited)
        q = queue.popleft()  # begin, cnt
        visited.append(q[0])

        if q[0] == target:
            return q[1]

        for word in words:
            if check(q[0], word) and word not in visited:
                queue.append((word, q[1]+1))

    return answer
