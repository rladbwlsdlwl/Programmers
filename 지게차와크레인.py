from collections import deque
import copy
def solution(storage, requests):

    R = len(storage)
    C = len(storage[0])
    visited = [[False for _ in range(C)] for __ in range(R)]
    dy, dx = [-1, 0, 1 , 0], [0, 1, 0, -1]

    def findOutside(r, c):
        # 바깥으로 나갈 수 있는 경로가 있는 경우 찾기
        q = deque()
        q.append((r, c))
        
        path = [[False for _ in range(C)] for __ in range(R)]
        while q:
            y, x = q.popleft()
            for i in range(4):
                movey, movex = dy[i]+y, dx[i]+x

                if movey == -1 or movex == -1 or movey >= R or movex >= C:
                    return True
                
                if visited[movey][movex] and not path[movey][movex]:
                    path[movey][movex] = True
                    q.append((movey, movex))

        return False
    
    
    for req in requests:
        if len(req) == 1:
            stk = []
            for i in range(R):
                for j in range(C):
                    if storage[i][j] == req and findOutside(i, j):
                        stk.append((i, j))
                        
                        
            while stk:
                y, x = stk.pop()
                visited[y][x] = True
        else:
            for i in range(R):
                for j in range(C):
                    if storage[i][j] == req[0]:
                        visited[i][j] = True
                        
    # print(visited)
        
    return sum(1 for j in range(C) for i in range(R) if not visited[i][j])
