import sys

input = sys.stdin.readline

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
        return True
    return False

line = input()
testCase = int(line)

edges = []
NArray = []
for i in range(testCase):
    line = input()
    N , M = line.split(" ")
    N , M = int(N), int(M)
    NArray.append(N)
    edges.append([])
    
    for j in range(M):
        line = input()
        a , b = line.split(" ")
        a , b = int(a), int(b)
        edges[i].append([a-1,b-1])
  
for i in range(testCase):
    mst = []
    parentNode = [-1] * NArray[i]

    for edge in edges[i]:
        if isCycle(parentNode,edge[0],edge[1]) == False:
            mst.append(edge)
            parentNode[edge[1]] = edge[0]
    print(len(mst))


