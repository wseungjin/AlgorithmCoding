# f = open("input.txt", 'r')
# line = f.readline()
line = input()

N=int(line)


array = [0] * 1000010

array[1] = 1
array[2] = 2

for i in range (3,N+1):
    array[i] = (array[i-1] + array [i-2])%15746
    
print(array[N])