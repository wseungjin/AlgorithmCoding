def isCycle(parentNode,leftIndex,rightIndex):
    leftRoot = parentNode[leftIndex]   
    while leftRoot != -1:
        leftIndex = leftRoot
        leftRoot = parentNode[leftIndex]   
        
    rightRoot = parentNode[rightIndex]   
    while rightRoot != -1:
        rightIndex = rightRoot
        rightRoot = parentNode[rightIndex]     
    
    if leftIndex == rightIndex:
        return True,leftIndex,rightIndex
    return False,leftIndex,rightIndex

edges = []

line = input()
N , M = line.split(" ")
N , M = int(N), int(M)

for j in range(M):
    line = input()
    a , b, c = line.split(" ")
    a , b, c = int(a), int(b) , int(c)
    edges.append([a-1,b-1,c])
        
edges = sorted(edges,key=lambda x:x[2])

mst = []  
parentNode = [-1] * N

answer = 0
for edge in edges:
    flag, leftIndex, rightIndex = isCycle(parentNode,edge[0],edge[1]) 
    if flag == False:
        mst.append(edge)
        answer += edge[2]
        parentNode[leftIndex] = rightIndex

print(answer)