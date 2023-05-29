def solution(line):
    answer = []
    n = len(line)
    stars = []
    INF = float('inf')
    minX, maxX, minY, maxY = INF, -INF, INF, -INF
    
    for i in range(0, n):
        for j in range(i+1, n):
            a, b, e = line[i][0], line[i][1], line[i][2]
            c, d, f = line[j][0], line[j][1], line[j][2]
            
            if a*d - b*c == 0: continue
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            
            if int(x) == x and int(y) == y :
                minX = min(minX, int(x))
                maxX = max(maxX, int(x))
                minY = min(minY, int(y))
                maxY = max(maxY, int(y))
                stars.append([int(x), int(y)])
    # print(stars)
    # print(minX, maxX, minY, maxY)
    
    answer = [['.' for x in range(maxX - minX + 1)] for y in range(maxY - minY + 1)]
    for star in stars:
        x = star[0]
        y = star[1]
        # print("x, y", x, y)
        answer[maxY - y][x-minX] = "*" # 새로운 배열의 좌표가 되려면
    return [''.join(s) for s in answer]