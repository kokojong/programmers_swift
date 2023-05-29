from itertools import product

def solution(word):
    answer = 0
    # A E I O U
    # 1 2 3 4 5 -> 6진수랑 비슷하게 생각
    
    # AAAA = 11110 = 4
    # AAAE = 11120 = 10 (6차이)
    
    # 앞에꺼 * 5 + 1 가짓수(아무것도 없는 경우)
    # A와 I의 차이 1562 / 2 = 781 (맨 앞에자리 차이)
    
#     mo = ['A', 'E', 'I', 'O', 'U']
#     diff = [1] 
#     k = 1
#     for i in range(4):
#         k = k * 5 + 1 # 똑같은거 5개 + 뒤에 암것도 없는거 1개
#         diff.append(k)
#     diff.reverse() # [781, 156, 31, 6, 1]
    
#     for i in range(len(word)):
#         w = word[i]
#         idx = mo.index(w)  # A - 0 ... U - 4
        
#         answer += diff[i] * idx + 1 # i번째 가중치 * 그만큼의 차이 + 1

    # return answer

    # 완탐 풀이법 with product
#     mo = ['A', 'E', 'I', 'O', 'U'] # 모음
#     words = []
#     for i in range(1, 6):
#         for c in product(mo, repeat=i):
#             words.append(''.join(list(c)))

#     words.sort() # 자동으로 이 순서대로 해준다.
#     return words.index(word) + 1
    
    # 완탐 풀이법 with dfs
    mo = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def dfs(l, s): # l: 길이, s: 문자열
        if l == 5:
            return
        
        for i in range(5):
            words.append(s + mo[i])
            dfs(l + 1, s + mo[i])
    dfs(0, "")    
    
    return words.index(word) + 1
    
    