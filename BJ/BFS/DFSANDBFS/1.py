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
        
    def sortGraph(self):
        self.graph=collections.OrderedDict(sorted(self.graph.items()))
        for i in self.graph.keys():
            self.graph[i] = sorted(self.graph[i])
                             
    # The function to do BFS traversal. It uses 
    def BFS(self,s):
        V=vNum
    
        visited = [False] * (V+1)
        
        queue=collections.deque()
        
        queue.append(s) 
        visited[0] = True
        visited[s] = True
        
        while queue :            
            s= queue.popleft()
            print (s, end = " ") 
            
            if s in self.graph:
                for i in self.graph[s] :
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
            
    # A function used by DFS 
    def DFSUtil(self, v,visited): 
        
        visited[v] = True
        print (v, end = " ") 
        
        if v in self.graph:
            for u in self.graph[v]:
                if visited[u] == False:
                    self.DFSUtil(u,visited)  
                
                
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self,start):
        V=vNum
    
        visited = [False] * (V + 1)
        
        visited[0] = True
        self.DFSUtil(start,visited)

        
       
g = Graph() 
 
# f = open("input.txt", 'r')
# line = f.readline()
line = input()

vNum , eNum , start = line.split(" ")
vNum , eNum , start = int(vNum) , int(eNum) , int(start) 

for i in range (eNum):
    line = input()
    # line = f.readline()     
    line = line.split(" ")
    
    g.addEdge(int(line[0]),int(line[1]))
    g.addEdge(int(line[1]),int(line[0]))
# f.close()

g.sortGraph()
g.DFS(start)
print()
g.BFS(start) 
  
# This code is contributed by Neelam Yadav 