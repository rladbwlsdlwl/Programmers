from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])
    visited = [[False for j in range(C)] for i in range(R)]

    
    def bfs(y, x):
        # 상하좌우 이동하며 방문
        
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        
        q = deque([(y, x)])
        visited[y][x] = True
        day = 0
        
        while q:
            r, c = q.popleft()
            day += int(maps[r][c])
            
            
            for i in range(4):
                movey, movex = dy[i] + r, dx[i] + c
                if movey >= R or movex >= C or movey < 0 or movex < 0:
                    continue
                
                
                if maps[movey][movex] != 'X' and not visited[movey][movex]:
                    q.append((movey, movex))
                    visited[movey][movex] = True
        
        return day
            
    # BFS
    # 방문 가능한 노드 찾기
    
    answer = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
    
    
    return sorted(answer) if len(answer) else [-1]
