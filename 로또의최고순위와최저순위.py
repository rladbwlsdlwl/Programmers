def solution(lottos, win_nums):
    ans = [7, 7]
    
    for i in range(len(lottos)):
        if lottos[i] == 0:
            ans[0] -= 1
            continue
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                ans[0] -= 1
                ans[1] -= 1
                break
    if ans[0] == 7:
        ans[0] = 6
    if ans[1] == 7:
        ans[1] = 6
    return ans
