def solution(arr):
    ans = []
    
    for n in arr:
        if len(ans)==0 or ans[-1] != n:
            ans.append(n)
            
    return ans
