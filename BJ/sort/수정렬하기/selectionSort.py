# f = open("input.txt", 'r')
# line = f.readline()
line = input()
num = int(line)

array = []

for i in range(num):
    # line = f.readline()
    line = input()
    array.append(int(line))
 
for i in range(len(array)):
    min = array[i]
    minIndex = i
    for j in range(i,len(array)):
        if min > array[j]:
            min = array[j]
            minIndex = j
    temp = array[i]
    array[i] = min
    array[minIndex] = temp
        
for i in range(num):
    print(array[i])