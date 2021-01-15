

array = [10,9,8,7,6,5,4,3,2,1,11,12,13,16,15,14,17,19,18,20]

n = len(array)

for i in range(1,n):
    print(array)
    insertedValue = array[i]
    nextIndex = i - 1
    while nextIndex >= 0:
        if insertedValue < array[nextIndex]:
            array[nextIndex+1] = array[nextIndex]
        else: 
            break
        nextIndex -= 1
    array[nextIndex + 1] = insertedValue
 
print(array)