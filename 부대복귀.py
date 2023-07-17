from collections import defaultdict
from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    # sources 에 대원들이 있고 destination으로 가야한다.(최단거리로) -> 이때의 거리를 return
    # roads를 돌면서 destination에서부터 source로 도착하는 거리를 각각 구하자!

    maxV = 10**6
    # graph = [[] for _ in range(n+1)]
    graph = defaultdict(list)
    for road in roads:
        s, e = road
        graph[s] += [e]
        graph[e] += [s]

    dis = [maxV for _ in range(n+1)]  # destination 부터 시작하기!
    visited = [False for _ in range(n+1)]

    queue = deque()
    queue.append([destination, 0])  # 시작점, 거리

    while queue:
        v, d = queue.popleft()
        if visited[v]:
            continue  # 방문한 노드면 패스

        visited[v] = True
        dis[v] = d

        for connect in graph[v]:
            queue.append([connect, d + 1])

    for source in sources:
        if dis[source] == maxV:
            answer.append(-1)
        else:
            answer.append(dis[source])

    return answer
