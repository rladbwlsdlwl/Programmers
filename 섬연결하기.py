# min heap

import heapq

def solution(n, costs):
    answer = 0
    
    # dijkstra
    graph = [[] for _ in range(n)]

    visited = [False for _ in range(n)]
    
    
    for cost in costs:
        # undirected graph
        # 양쪽 연결
        graph[cost[0]].append((cost[1], cost[2]))
        graph[cost[1]].append((cost[0], cost[2]))
        
    
        
    # 방문 가능한 모든 간선 리스트
    # 간선이 짧은 순으로 방문
    # 이미 방문한 노드는 방문하지 않음
    hq = [(0, 0)] # (간선 가중치, 도착지노드)
    
    cnt = 0
    while hq:
        
        w, goal = heapq.heappop(hq)
        
        if visited[goal]:
            continue
            
            
        visited[goal] = True
        
        answer += w
        cnt += 1
        
        if cnt == n:
            break
        
        for node, weight in graph[goal]:
            
            if not visited[node]:
                heapq.heappush(hq, (weight, node))
        
        
    
    
    return answer
