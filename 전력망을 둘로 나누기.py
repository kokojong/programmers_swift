import copy
import sys
sys.setrecursionlimit(10**7)

def solution(n, wires):
    answer = n
    # n 이 100이하 -> 완탐?
    # wires도 길이가 n-1 -> 완탐
    
    
    def dfs(k, w, result, visited): # k: 현재 노드 번호, cnt: 현재 연결 된 갯수, w: 현재 wire 상태, result: connect 된 애들의 list
        visited[k-1] = True
        result.append(k)
        
        for ww in w:
            if ww[0] == k and visited[ww[1]-1] == False : # k에서 시작(더 작음)
                dfs(ww[1], w, result, visited)
            elif ww[1] == k and visited[ww[0]-1] == False:
                dfs(ww[0], w, result, visited)
                
        return result
        
        
    
    for wire in wires:
        tmp = copy.deepcopy(wires)
        tmp.remove(wire)
        result = dfs(1, tmp, [], [False] * n) # 연결된 애들의 list
        a = abs(n - len(result) * 2) # 차이의 절댓값
        answer = min(answer, a)
    
    return answer