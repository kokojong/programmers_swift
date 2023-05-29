from collections import deque

def solution(s):
    answer = 0
    dq = deque(s)
    for _ in range(len(s)):
        dq.append(dq.popleft())
        stack = []
        
        for q in dq:
            if not stack:
                stack.append(q)
                continue
            last = stack[-1]
            
            if q in [']', '}', ')']:
                if q == ']' and last == '[':
                    stack.pop()
                elif q == '}' and last == '{':
                    stack.pop()
                elif q == ')' and last == '(':
                    stack.pop()
                else:
                    stack.append(q)
            else:
                stack.append(q)
        if not stack:
            answer += 1
    
    # print(list(dq))
    
    return answer