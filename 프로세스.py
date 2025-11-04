from collections import deque

def solution(priorities, location):
    answer = 0
    
    
    # (값, 인덱스) 순으로 큐에 push
    
    q = deque()
    for idx, order in enumerate(priorities):
        q.append((order, idx))


    while q:
        # q 배열에서 우선순위(1 ~ 9)가 가장 높은 작업 찾기
        mx, i = max(q)
        
        stopped_idx = -1
        # 우선순위가 높은 작업 찾아 실행
        while True:
            p, idx = q.popleft()
            
            # 우선순위가 낮은 경우
            if p != mx:
                q.append((p, idx))
            
            # 우선순위가 높아 실행할 프로세스일 경우
            if p == mx:
                answer += 1
                stopped_idx = idx
                break
                
                
        # 실행한 프로세스가 찾는 프로세스일 경우
        if stopped_idx == location:
            return answer
                
