def solution(n, results):
    answer = 0

    # 플로이드 와샬 알고리즘 -> 중간지점을 먼저 잡고, i -> j로 갈때 k를 거치는걸 체크
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]  # 0은 안쓰기

    for result in results:
        win, lose = result
        graph[win][lose] = 1
        graph[lose][win] = -1
    # print(graph)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:  # k는 i한테 지고, j한테 이긴거면
                    graph[i][j] = 1
                    graph[j][i] = -1
    # print(graph)
    for g in graph:
        if g.count(0) == 2:  # 자기 자신, 0에는 미방문
            answer += 1

    return answer
