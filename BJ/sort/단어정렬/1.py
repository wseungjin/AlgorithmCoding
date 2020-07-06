# f = open("input.txt", 'r')
# line = f.readline()
line = input()
num = int(line)

array = []

for i in range(num):
    # line = f.readline()
    line = input()
    if not(line in array):
        array.append(line)
 
array = sorted(array)
array = sorted(array, key=lambda x:len(x))

for i in array:
    print(i)
