def sort(arr):
    if(len(arr)==1):
        return arr

    else:
        mid=len(arr)//2
        left=merge_sort(arr[0:mid])
        right=merge_sort(arr[mid:])
        return merge(left,right)

def merge(left,right):
    sortArray=[]
    left_idx,right_idx=0,0

    while(left_idx<len(left) and right_idx<len(right)):
        if(left[left_idx]>right[right_idx]):
            sortArray.append(right[right_idx])
            right_idx+=1
        else:
            sortArray.append(left[left_idx])
            left_idx+=1

    if(left_idx==len(left)):
        sortArray+=right[right_idx:]
    if(right_idx==len(right)):
        sortArray+=left[left_idx:]

    return sortArray
def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        answer.append(merge_sort(array[commands[i][0]-1 : commands[i][1]])[commands[i][2]-1])

    return answer
