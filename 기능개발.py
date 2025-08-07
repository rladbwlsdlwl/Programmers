def solution(progresses, speeds):
    answer = []
    
    N = len(progresses)
    p = 0
    
    while p < N:
        # 작업이 얼마나 남았는지, 몇일 뒤에 완료되는지 계산
        job = 100-progresses[p]
        time = job//speeds[p] if job % speeds[p] == 0 else job//speeds[p] + 1 
        
        cnt = 0
        flag = True
        for i in range(p, N):
            progresses[i] += speeds[i] * time
            
            if flag and progresses[i] >= 100:
                progresses[i] = 100
                p += 1
                cnt += 1
            else: 
                flag = False
        
        answer.append(cnt)
    
    return answer
