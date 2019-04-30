your_list:list =  [5,2,3,1,88,33,7,10,17,32,66,101,9,8]

def linear_search(arr:list, value:int) -> int:
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

result:int = linear_search(your_list,7)
print(result)
