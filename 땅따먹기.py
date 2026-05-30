def solution(land):

    # Greedy (밑 행에서 각 열에서 가질 수 있는 최댓값 찾기)
    # 16*10^5 = 10^6
    N = len(land)
    for i in range(N-1):
        
        # 4*4
        for j in range(4):
            mx = max(list(land[i][p] for p in range(4) if j != p)) # 동일 열이 아닌 최대 값
            
            land[i+1][j] += mx
    # print(land)
    return max(land[-1])
    
        
