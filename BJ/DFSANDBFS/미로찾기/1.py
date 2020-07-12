from collections import defaultdict
import collections 
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
                             
    # The function to do BFS traversal. It uses 
    def BFS(self,N,M,start):    
        visited=[[False for i in range(M)] for j in range(N)]
        dist=[[0 for i in range(M)] for j in range(N)]
                
        queue=collections.deque()
        queue.append(start) 
        visited[start[0]][start[1]] = True
        dist[start[0]][start[1]] = 1
        
        while queue :            
            s= queue.popleft()
            
            if s in self.graph:
                for i in self.graph[s] :
                    if visited[i[0]][i[1]] == False:
                        dist[i[0]][i[1]] = dist[s[0]][s[1]] + 1    
                        queue.append(i)
                        visited[i[0]][i[1]] = True
                        
        print(dist[N-1][M-1])
                        
                        
        
       
g = Graph() 
 
# f = open("input.txt", 'r')
# line = f.readline()
line = input()

N, M = line.split(" ")
N, M = int(N) , int(M)
array=[[0 for i in range(M)] for j in range(N)]

for i in range (N):
    # line = f.readline()     
    line = input()
    for j in range (M):
        array[i][j] = int(line[j])


for i in range (N):
    for j in range (M):
        if j-1>-1 and array[i][j-1]:
            g.addEdge((i,j),(i,j-1))    
        if i-1>-1 and array[i-1][j]:
            g.addEdge((i,j),(i-1,j))    
        if j+1<M and array[i][j+1]:
            g.addEdge((i,j),(i,j+1))    
        if i+1<N and array[i+1][j]:
            g.addEdge((i,j),(i+1,j))    
        

# f.close()
g.BFS(N,M,(0,0)) 
  
