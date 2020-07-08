import sys

# f = open("input.txt", 'r')
# line = f.readline()

line = input()
# line = f.readline()

line = line.replace("\n","")
N=int(line)

answer = [0] * N

array = list(map(int, sys.stdin.readline().split())) 

answer[0] = array[0]
result=answer[0]

for i in range(1,N):
    answer[i]=max(answer[i-1]+array[i],array[i])
    result=max(answer[i],result)

print(result)