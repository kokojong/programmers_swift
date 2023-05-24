import copy

def solution(skill, skill_trees):
    answer = 0
    s = list(skill)
    s.reverse()
    
    for skill_tree in skill_trees:
        stack = copy.deepcopy(s)
        for skill in skill_tree:
            if skill in stack: # stack에 있는 애면(스킬트리에 포함된 애면)
                p = stack.pop()
                if p != skill:
                    break
                    # continue # 스킬트리 맨 위에 있는게 아니라면 continue
        
        else: answer += 1 # 다 통과하면 +=1 
    
    return answer