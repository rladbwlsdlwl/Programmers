def solution(triangle):
    # bottom up
    N = len(triangle)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1):
            left = dp[i][j] + triangle[i+1][j]
            right = dp[i][j] + triangle[i+1][j+1]
            dp[i+1][j] = max(dp[i+1][j], left)
            dp[i+1][j+1] = max(dp[i+1][j+1], right)
            
    return max(dp[N-1]) + triangle[0][0]
