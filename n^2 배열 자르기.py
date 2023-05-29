def solution(n, left, right):
    answer = []
    
    # 처음에는 직접 보드를 만들려고 했는데 n이 10**7이라서 바로 수정
    r1, c1 = left//n, left%n
    r2, c2 = right//n, right%n
    # print(r1, c1, r2, c2)
    # for r in range(r1, r2 + 1):
    #     row = [0] * n
        # k = r + 1 # 실제로 들어가는 값은 r + 1
        # for i in range(n):
            # if i > r:
            #     k += 1
            # row[i] = k
#             row[i] = max(i, r) + 1
            
#         if r == r1:
#             answer.extend(row[c1:])
#         elif r == r2:
#             answer.extend(row[:c2+1])
#         else:
#             answer.extend(row)
            
    # extend를 써서 실패가 뜸 2, 15~20번 케이스
    for i in range(left, right + 1):
        r = i // n
        c = i % n
        answer.append(max(r, c) + 1)
    return answer