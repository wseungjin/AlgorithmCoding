# f = open("input.txt", 'r')
# line = f.readline()
array =[[0 for i in range(2)] for j in range (41)]

array[0][0] = 1
array[1][1] = 1

for i in range (2,41):
    array[i][0] = array[i-1][0] + array [i-2][0]
    array[i][1] = array[i-1][1] + array [i-2][1]

line = input()
# line = f.readline()

line = line.replace("\n"," ")
N=int(line)

for i in range(N):
    line = input()
    # line = f.readline()
    line = line.replace("\n"," ")

    M=int(line)
    print(str(array[M][0])+" "+str(array[M][1]))