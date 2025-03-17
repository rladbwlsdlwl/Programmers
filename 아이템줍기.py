def solution(rectangle, characterX, characterY, itemX, itemY):
    maze = [[-1 for _ in range(102)] for _ in range(102)]
    
    # 1. init
    # -1 -1 -1 -1 -1
    # -1  1  1  1 -1
    #  1  1  0  1 -1
    #  1  1  1  1 -1
    # -1 -1 -1 -1 -1
    
    # 1.1 겹치는 변을 위해 사각형 2배씩 늘리기
    # 1.2 답 // 2
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if (i == y1 or i == y2 or j == x1 or j == x2) and maze[i][j] != 0: # 이미 사각형이 있는 부분은 그리지 않음
                    maze[i][j] = 1
                else:
                    maze[i][j] = 0
                    
    
    # 2. 둘레 따라 움직이기
    visited = [[False for _ in range(102)] for _ in range(102)]
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    def dfs(r, c):
        if r == itemY and c == itemX:
            return 0
        
        visited[r][c] = True
        for i in range(4):
            movey, movex = r+dy[i], c+dx[i]
            
            if not visited[movey][movex] and maze[movey][movex] == 1:
                return 1 + dfs(movey, movex)
            
        
    return min(dfs(characterY, characterX), dfs(characterY, characterX)) // 2
