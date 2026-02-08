def solution(myString, pat):
#     stk = []
    
#     N = len(myString)
#     M = len(pat)
    
#     ans = ""
#     for i in range(N):
#         stk.append(myString[i])
        
        
#         if i < M-1:
#             continue
            
#         # PEEK
#         valid = True
#         for j in range(M):
#             if stk[-M+j] != pat[j]:
#                 valid = False
#                 break
       

#         if valid:
#             ans = "".join(stk)
        
            
#     return ans


    return myString[0: myString.rfind(pat)] + pat
