def solution(record):
    answer = []
    
    table = {}
    
    # 최종 유저명 기록
    for line in record:
        l = line.split(" ")
        
        if len(l) == 2: # leave
            continue
        else: # enter OR change
            comm, uid, username = l
            
            table[uid] = username
    
    # enter/leave 기록
    for line in record:
        l = line.split(" ")
        
        
        currentName = table[l[1]]
        if l[0] == "Enter":
            answer.append(currentName + "님이 들어왔습니다.")
        elif l[0] == "Leave":
            answer.append(currentName+ "님이 나갔습니다.")
            
    
    return answer
