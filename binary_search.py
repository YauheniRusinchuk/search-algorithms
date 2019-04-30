your_list:list =  [5,2,3,1,88,33,7,10,17,32,66,101,9,8]


def binary_search(arr:list, value:int) -> int:
    low:int     = 0
    high:int    = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if value < arr[mid]:
            high = mid - 1
        elif value > arr[mid]:
            low = mid + 1
        else:
            return mid

    else:
        return -1


result:int =  binary_search(your_list, 66)
print(result)
