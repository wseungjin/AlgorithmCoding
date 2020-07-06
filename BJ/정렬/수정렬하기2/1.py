# f = open("input.txt", 'r')
# line = f.readline()
line = input()
num = int(line)

array = []

for i in range(num):
    # line = f.readline()
    line = input()
    array.append(int(line))

array=sorted(array)

for i in range(num):
    print(array[i])
