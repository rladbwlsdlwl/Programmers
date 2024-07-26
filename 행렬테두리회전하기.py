def solution(rows, columns, queries):
    arr = [[(i+1) + columns*j for i in range(columns)] for j in range(rows)]
    
    ans = []
    for y1, x1, y2, x2 in queries:
        y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
        mn = 10000
        # >
        rem = arr[y1][x1]
        for i in range(x1, x2):
            arr[y1][i+1], rem = rem, arr[y1][i+1]
            mn = min(mn, rem)
            
        # V
        for i in range(y1, y2):
            arr[i+1][x2], rem = rem, arr[i+1][x2]
            mn = min(mn, rem)
        
        # < 
        for i in range(x2, x1, -1):
            arr[y2][i-1], rem = rem, arr[y2][i-1]
            mn = min(mn, rem)
        
        # ^
        for i in range(y2, y1, -1):
            arr[i-1][x1], rem = rem, arr[i-1][x1]
            mn = min(mn, rem)
            
        ans.append(mn)
        
        
    return ans
