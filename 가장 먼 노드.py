from collections import defaultdict


def solution(n, edges):
    answer = [0 for _ in range(n)]

    global maxDistance
    maxDistance = 0
    connected = defaultdict(list)  # i 입장에서 연결이 된 모음
    visited = [False for _ in range(n)]

    for edge in edges:
        a, b = edge[0] - 1, edge[1] - 1
        connected[a].append(b)
        connected[b].append(a)

    def bfs(k, visited):
        queue = []
        queue.append((0, 0))
        global maxDistance

        while queue:
            q, l = queue.pop(0)
            visited[q] = True

            for c in connected[q]:  # q와 연결된 애들
                if visited[c] == False:
                    visited[c] = True
                    queue.append((c, l+1))
                    maxDistance = max(maxDistance, l+1)
                    answer[c] = l+1

    bfs(0, visited)

    return answer.count(maxDistance)
