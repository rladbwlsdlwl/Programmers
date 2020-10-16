def merge_sort(arr):
        if(len(arr)==1):
            return arr
        mid=len(arr)//2 
        left=merge_sort(arr[0:mid])
        right=merge_sort(arr[mid:])
        return merge(left,right)

def merge(left,right):
    sortArr=[]
    i=0;j=0
        
    while(i<len(left) and j<len(right)):
        if(int(str(left[i])+str(right[j])) > int(str(right[j])+str(left[i]))): #331 313
            sortArr.append(left[i]); i+=1
        else:
            sortArr.append(right[j]); j+=1 
                        
    if(i==len(left)):
        sortArr+=right[j:]
    if(j==len(right)):
        sortArr+=left[i:]
            
    return sortArr

def solution(numbers):
    if(numbers.count(0)==len(numbers)):
        return "0"
    
    return "".join(map(str,merge_sort(numbers)))
