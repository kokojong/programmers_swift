def solution(cards):
    answer = 0
    # idea: cycle이 여러개가 되니까 사이클에 들어있는 갯수를 arr로 저장. sort후 큰거부터 2개 선택!
    n = len(cards)
    
    visited = [False] * (n+1)
    cycles = [] 
    
    for i in range(n): # 0 ~ n-1
        x = i # now
        c = 0
        while not visited[x+1]:
            c += 1
            visited[x+1] = True # visited[1] 
            next = cards[x] # 8
            x = next - 1
            cycles.append(c)
    cycles.sort()
    
    answer = cycles[-1] * cycles[-2]
    
    return answer