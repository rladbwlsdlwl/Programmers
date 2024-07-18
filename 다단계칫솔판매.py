import sys
sys.setrecursionlimit(20000)

def solution(enroll, referral, seller, amount):
    hash = {}
    graph = [[] for _ in range(len(enroll))]
    for i, name in enumerate(enroll):
        hash[name] = i
        
    
    for i in range(len(enroll)):
        node1, node2 = hash[enroll[i]], referral[i]
        
        if node2 == "-":
            continue
            
        node2 = hash[node2]
        graph[node1].append(node2)
    
    ans = [0 for _ in range(len(enroll))]
    def dfs(node, money):
        if money <= 1: # 1원이하 벌었을 경우
            ans[node] += money
            return 
        
        earn, give = money - int(money * 0.1), int(money * 0.1)
        ans[node] += earn
        
        if len(graph[node]) == 0: # 상위노드가 없을경우
            return 
        dfs(graph[node][0], give)
        
    
    
    for i, name in enumerate(seller):
        node = hash[name]
        dfs(node, amount[i]*100)
        
    return ans
