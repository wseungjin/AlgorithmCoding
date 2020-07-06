# f = open("input.txt", 'r')
# line = f.readline()
line = input()
num = int(line)

array = []

for i in range(num):
    # line = f.readline()
    line = input()
    array.append(int(line))
 
for i in range(len(array)-1,0,-1):
    for j in range(i):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]  
            array[j+1] = temp

for i in range(num):
    print(array[i])