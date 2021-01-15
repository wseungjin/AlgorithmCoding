

array = [10,9,8,7,6,5,4,3,2,1,11,12,13,16,15,14,17,19,18,20]

n = len(array)

for i in range(n):
    minValue = array[i]
    minIndex = i
    for j in range(i+1,n):
        if minValue > array[j]:
            minValue = array[j]
            minIndex = j
            
    temp = array[i]
    array[i] = minValue
    array[minIndex] = temp
print(array)