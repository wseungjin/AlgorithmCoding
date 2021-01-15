

array = [10,9,8,7,6,5,4,3,2,1,11,12,13,16,15,14,17,19,18,20]

n = len(array)

for i in range(n):
    for j in range(n - 1):
        if array[j] > array [j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            
print(array)