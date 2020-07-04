from collections import defaultdict 
  
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
                
                
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def BFS(self,s):
        V=len(self.graph) 
    
        visited = [False] * V
        
        queue = [] 
        
        queue.append(s) 
        visited[s] = True
        
        while queue :
            
            s= queue.pop()
            print (s, end = " ") 
            
            for i in self.graph[s] :
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
            
        
            
                
                
                
            
                
            
            
        
        

  
  
# Driver code 
# Create a graph given in the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is BFS")
g.BFS(0) 
  
# This code is contributed by Neelam Yadav 