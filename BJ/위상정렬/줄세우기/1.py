from collections import deque

# f = open("input.txt", 'r')
# line = f.readline()
line = input()

N , M = line.split(" ")
N , M= int(N) , int(M)

arr = []

for i in range(M):
    # line = f.readline()
    line = input()

    A, B = line.split(" ")
    A, B = int(A) , int(B)
    arr.append([A, B])
    
inDegree = [ 0 for i in range(32001)] 
graph = [[] for i in range(32001)]
queue = deque()

for a, b in arr: 
    inDegree[b] += 1 
    graph[a].append(b)

for index in range(1,N+1):
    if inDegree[index] == 0:
        queue.append(index)

while queue:
    current = queue.popleft()
    for index in graph[current]:
        inDegree[index] -= 1 
        if inDegree[index] == 0:
            queue.append(index)        
    print(current, end = " ")   
        
    
                    


        
        

    
    