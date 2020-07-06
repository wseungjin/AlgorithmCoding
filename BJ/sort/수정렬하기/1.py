# f = open("input.txt", 'r')
# line = f.readline()
line = input()
num = int(line)

array = []
sortedArray =[]

for i in range(num):
    # line = f.readline()
    line = input()
    array.append(int(line))
 
for i in range(len(array)):
    min = array[0]
    minIndex = 0
    for j in range(len(array)):
        if min > array[j]:
            min = array[j]
            minIndex = j
    sortedArray.append(min)
    array.pop(minIndex)
        
for i in range(num):
    print(sortedArray[i])
