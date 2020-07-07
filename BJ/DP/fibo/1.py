# f = open("input.txt", 'r')
# line = f.readline()
line = input()

N=int(line)


array = [0] * (N+1)

array[1] = 1

for i in range (2,N+1):
    array[i] = array[i-1] + array [i-2]
    
print(array[N])