def solution(numbers, target):
    def dfs(i, curr_sum): # index, 누적 값
        ans = 0
        if i == len(numbers):
            return 1 if curr_sum == target else 0
        
        ans += dfs(i+1, curr_sum + numbers[i])
        ans += dfs(i+1, curr_sum - numbers[i])
        
        return ans
        
    
    return dfs(0, 0)
