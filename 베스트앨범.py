def solution(genres, plays):
    table = {}
    
    for i in range(len(genres)):
        g, cnt = genres[i], plays[i]
        
        if g in table:
            table[g][0] += cnt
            
            if plays[table[g][1][0]] < cnt:
                table[g][1][0], table[g][1][1] = i, table[g][1][0]
            elif table[g][1][1] == -1 or plays[table[g][1][1]] < cnt:
                table[g][1][1] = i
                         
        else:
            table[g] = [cnt, [i, -1]] # [sum, (max, second_max)]
            
    
    ans = []
    table_list = list(table.values())
    table_list.sort(key = lambda x: x[0], reverse = True)
    
    print(table_list)
    for val, idx_list in table_list:
        if idx_list[1] == -1:
            ans.append(idx_list[0])
        else:
            ans.extend(idx_list)
                         
    return ans
