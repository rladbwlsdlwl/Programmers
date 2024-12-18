def solution(nums):
    TYPE = 200000+1
    table = [0 for _ in range(TYPE)]
    
    for i in range(len(nums)):
        table[nums[i]] += 1
        
    ans = 0
    for i in range(1, TYPE):
        if table[i]:
            ans += 1
        if ans == len(nums) // 2:
            break
            
    return ans
