# f = open("input.txt", 'r')
# line = f.readline()

line = input()
# line = f.readline()

line = line.replace("\n"," ")
N=int(line)


array = [0] * N

answer = [0] * N

line = input()
# line = f.readline()
line = line.replace("\n"," ")

for i in range(N):
    array[i]= int(line.split(" ")[i])

answer[0] = 1


for i in range(1,N):
    max = 0
    for j in range(i,-1,-1):
        if array[i]>array[j] and (max==0 or max<answer[j]):    
            max = answer[j]
    answer[i] = max + 1
answer=sorted(answer)
print(answer[N-1])