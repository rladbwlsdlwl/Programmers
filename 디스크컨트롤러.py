import heapq

def solution(jobs):
    # Non Preemptive
    # 우선 순위: 짧은 작업 > 먼저 요청한 작업 > 작은 작업 번호 
    # min heap 
    
    
    
    jobs.sort()
    
    top = jobs[0]
    hq = []
    
    heapq.heappush(hq, (top[1], top[0], 0))
    
    i = 1
    N = len(jobs)
    all_turnaround = 0
    curr_time = top[0]
    while hq:
        time, reqTime, idx = heapq.heappop(hq)
        
        # 누적시간 카운팅
        curr_time += time
        # 반환 시간 계산
        all_turnaround += curr_time - reqTime
        
        
        # 요청 작업 순서 정리
        while i < N:
            rt, t = jobs[i]
            
            if len(hq) == 0 and rt > curr_time:
                curr_time = rt
            if rt > curr_time : break
            
            heapq.heappush(hq, (t, rt, i))
            i += 1
        
        
    
        
    return all_turnaround//N
