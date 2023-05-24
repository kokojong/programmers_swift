def solution(n):
    answer = []
    
    arr = [[0] * n for _ in range(n)] # n * n
    end = n * n - (n)*(n-1) //2 # 총 갯수
    # idea: -1, 0에서 부터 시작해서 
    r = -1
    c = 0
    num = 1
    # down, right, up 순서가 반복된다
    # n, n-1, n-2 ... 순으로
    for i in range(n): # 방향 전환이 될 때마다 올라가는게 i
        for j in range(i, n):
            # print(i, j)
            if i % 3 == 0:
                r += 1
            elif i % 3 == 1:
                c += 1
            else:
                r -= 1
                c -= 1
                
            arr[r][c] = num
            num += 1
    
    # print(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                answer.append(arr[i][j])
    
    return answer