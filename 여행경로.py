def solution(tickets):
    ans = []
    
    N = len(tickets)
    visited = [False for _ in range(N)]
    
    def dfs(position, path): # 현재 위치하고 있는 나라, 진입 경로
        if len(path) == N:
            path = path + [position]
            ans.append(path)
            return 
        
        for i, [start, end] in enumerate(tickets):
            if not visited[i] and position == start:
                visited[i] = True
                dfs(end, path + [start])
                visited[i] = False
    
    dfs("ICN", [])
    ans.sort(key = lambda x: x)
    
    return ans[0]
