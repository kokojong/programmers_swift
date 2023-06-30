def solution(n, computers):
    answer = set()
    parents = [i for i in range(n)]

    def find(a, parent):
        if parent[a] != a:
            parent[a] = find(parent[a], parent)

        return parent[a]

    def union(a, b, parent):
        parentA = find(a, parent)
        parentB = find(b, parent)

        if parentA < parentB:
            parent[parentA] = parentA
            parent[parentB] = parentA
        else:
            parent[parentA] = parentB
            parent[parentB] = parentB
        computers[parentA][parentB] = 1  # 연결해버림
        computers[parentB][parentA] = 1

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j, parents)
    for i in range(n):
        p = find(i, parents)
        answer.add(p)

    return len(answer)

# TC 9번 반례
# n = 7,
# computers = [[1, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1]]
# answer = 1
