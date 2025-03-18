import heapq
def solution(scoville, K):
    hq = []
    
    for scov in scoville:
        heapq.heappush(hq, scov)
        
    ans = 0 
    while hq:
        p1 = heapq.heappop(hq)
        
        if p1 >= K: return ans
        if not hq: break
        
        p2 = heapq.heappop(hq)
        
        heapq.heappush(hq, p1 + p2 * 2)
        ans += 1
        
        
    return -1
