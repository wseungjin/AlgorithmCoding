# f = open("input.txt", 'r')
# line = f.readline()
line = input()

line = line.replace("\n","")
line = line.split(" ")
N=int(line[0])
W=int(line[1])


array = [[0 for i in range(2)] for j in range(N+1)]



for i in range (1,N+1):
    # line = f.readline()
    line = input()
    line = line.replace("\n","")
    line = line.split(" ")
    array[i][0]=int(line[0])
    array[i][1]=int(line[1])

    
answer = [[0 for i in range(W+1)] for j in range(N+1)]


for i in range (1,N+1):
    for j in range (1,W+1):
        if(j-array[i][0]>=0):
            answer[i][j]=max(answer[i-1][j],answer[i-1][j-array[i][0]]+array[i][1])
        else:
            answer[i][j]=answer[i-1][j]
        
print(answer[N][W])

    
    
    
