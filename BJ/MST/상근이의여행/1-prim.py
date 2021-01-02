# f = open("input.txt", 'r')

# line = f.readline()
line = input()
testCase = int(line)

edges = [[] for k in range(testCase)] 
NMArray = []
for i in range(testCase):
    line = input()
    N , M = line.split(" ")
    N , M = int(N), int(M)
    NMArray.append((N,M))
    
    for j in range(M):
        line = input()
        a , b = line.split(" ")
        a , b = int(a), int(b)
        edges[i].append([a-1,b-1])
        
        

for i in range(testCase):
    N = NMArray[i][0]
    mst = []
    visited = [False] * N

    queue = []
    queue.append(0)
    count = 0
    while queue:
        current = queue.pop(0)
        visited[current] = True
        
        if count == N-1 :
            break

        for edge in edges[i]:
            if edge[0] == current and visited[edge[1]] == False:
                mst.append(edge)
                queue.append(edge[1])
                count += 1
            elif edge[1] == current and visited[edge[0]] == False:
                mst.append(edge)
                queue.append(edge[0]) 
                count += 1
    
    print(len(mst))


