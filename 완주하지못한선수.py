def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for idx,s in enumerate(participant):
        if idx==len(participant)-1 or s!=completion[idx]:
            answer+=s
            break
            
    return answer
