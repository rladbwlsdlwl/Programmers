def solution(s):
    answer = 0
    
    for i in range(len(s)):
        palindrome = s[i: ] + s[0: i]
        
        stk = []
        stopped = False
        for pal in palindrome:
            if pal == '(' or pal == '[' or pal =='{':
                stk.append(pal)
            else:
                # 닫힌 괄호가 매칭이 안되는 경우 || 괄호가 없는 경우
                if len(stk) == 0:
                    stopped = True
                    break
                
                p = stk.pop()
                
                if not (p == '(' and pal == ')' or p == '{' and pal == '}' or p == '[' and pal == ']'):
                    stopped = True
                    break
                
                
        if not stopped and len(stk) == 0: # 모든 괄호가 매칭된 경우
            answer += 1 
            
        
        
    return answer
