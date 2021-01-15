

array = [10,9,8,7,6,5,4,3,2,1,11,12,13,16,15,14,17,19,18,20]

n = len(array)

def merge(leftArray,rightArray):
    
    newArray = []
    leftArrayIndex = 0
    rightArrayIndex = 0
    
    while len(leftArray) > leftArrayIndex and len(rightArray) > rightArrayIndex:
        if leftArray[leftArrayIndex] < rightArray[rightArrayIndex]:
            newArray.append(leftArray[leftArrayIndex])
            leftArrayIndex += 1
        else:
            newArray.append(rightArray[rightArrayIndex])
            rightArrayIndex += 1
    
    while len(leftArray) > leftArrayIndex:
        newArray.append(leftArray[leftArrayIndex])
        leftArrayIndex += 1
        
    while len(rightArray) > rightArrayIndex:
        newArray.append(rightArray[rightArrayIndex])
        rightArrayIndex += 1
        
    return newArray

def mergeSort(array,left,right):
    
    if left == right:
        return [array[left]]
    
    mid = (left + right) // 2
    
    leftArray = mergeSort(array,left,mid) 
    rightArray = mergeSort(array,mid+1,right)
    
    return merge(leftArray,rightArray)
        
sortedArray = mergeSort(array,0,n-1)

print(sortedArray)