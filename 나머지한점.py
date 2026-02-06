from collections import defaultdict

def solution(v):
    table_x = defaultdict(int)
    table_y = defaultdict(int)
    
    
    for x, y in v:
        table_x[x] += 1
        table_y[y] += 1
        
    x, y = 0, 0
    for key in table_x:
        if table_x[key] == 1:
            x = key
            
    for key in table_y:
        if table_y[key] == 1:
            y = key
            
    return [x, y]
