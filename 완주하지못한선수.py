from collections import Counter
def solution(participant, completion):
    answer = ''
    table=Counter()
    
    for s in participant:
        table[s]+=1
        
    for s in completion:
        table[s]-=1
        
    for key,value in table.items():
        if value==1:
            answer+=key
            break
            
    return answer
