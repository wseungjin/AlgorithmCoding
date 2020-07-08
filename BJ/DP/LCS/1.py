array1 = [] 
array2 = []

# f = open("input.txt", 'r')
# line = f.readline()

line = input()

line = line.replace("\n","")

N = len(line)

for i in range(N):
    array1.append(line[i])



# line = f.readline()
line = input()

line = line.replace("\n","")

M = len(line)

for i in range(M):
    array2.append(line[i])

answer = [[0 for j in range(M+1)] for i in range(N+1)] 

for i in range(1,N+1):
    for j in range(1,M+1):
        if(array1[i-1]==array2[j-1]):
            answer[i][j] = answer[i-1][j-1] + 1
        else: 
            answer[i][j] = max(answer[i][j-1],answer[i-1][j]) 
        

print(answer[N][M])
