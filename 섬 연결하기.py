def solution(n, costs):
    answer = 0

    # visited = [] # 방문한 번호를 모아두는 배열
    parent = [i for i in range(n)]  # 각각의 부모를 연결 시작은 본인

    costs = sorted(costs, key=lambda x: x[2])  # 낮은 cost순으로 정렬

    def findParent(parent, a):
        if parent[a] == a:
            return a

        parent[a] = findParent(parent, parent[a])
        return parent[a]

    def unionParent(parent, a, b):
        parentA = findParent(parent, a)
        parentB = findParent(parent, b)

        if parentA == parentB:
            return parentA

        if parentA < parentB:
            parent[parentB] = parentA  # 더 작은거로 부모 갱신
        else:
            parent[parentA] = parentB
        return -1

    cnt = 0  # 연결된 갯수
    for cost in costs:
        a, b, c = cost

        if cnt == n:
            break
        if unionParent(parent, a, b) == -1:
            cnt += 1
            answer += c

    # for cost in costs:
    #     if len(visited) == n:
    #         break
    #     a, b, c = cost # a와 b 연결에 c만큼 소요
    #     if a not in visited and b not in visited:
    #         visited.append(a)
    #         visited.append(b)
    #         parent[a] = min(a, b) # 더 작은걸 parent로 부여
    #         parent[b] = min(a, b)
    #         answer += c
    #     elif a in visited and b not in visited:
    #         visited.append(b)
    #         parent[b] = parent[a] # a 랑 같은 부모로 취급함
    #         answer += c
    #     elif a not in visited and b in visited:
    #         visited.append(a)
    #         parent[a] = parent[b]
    #         answer += c
    return answer
