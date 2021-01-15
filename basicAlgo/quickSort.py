

array = [10,9,8,7,6,5,4,3,2,1,11,12,13,16,15,14,17,19,18,20]

n = len(array)

def partition(array,left,right):
    
    pivot = left
    
    low = left + 1 
    high = right
    
    while low <= high:
        if array[pivot] > array[high] and array[pivot] < array[low]:
            temp = array[high]
            array[high] = array[low]
            array[low] = temp
            high -= 1
            low += 1
        elif array[pivot] <= array[high] and array[pivot] >= array[low]:
            high -= 1
            low += 1
        elif array[pivot] <= array[high]:
            high -= 1
        elif array[pivot] >= array[low]:
            low += 1
            
    temp = array[high]
    array[high] = array[pivot]
    array[pivot] = temp
    
    return high
    
def quickSort(array,left,right):
    if left >= right:
        return
    
    newIndex = partition(array,left,right)
    quickSort(array,left,newIndex - 1)
    quickSort(array,newIndex + 1 , right)

quickSort(array,0,n-1)
            
print(array)