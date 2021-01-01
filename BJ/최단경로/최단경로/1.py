from collections import defaultdict


f = open("input.txt", 'r')
line = f.readline()
# line = input()

INF = -1

V , E = line.split(" ")
V , E= int(V) , int(E)

line = f.readline()
# line = input()
start = int(line)
start = start - 1

graph =  defaultdict(list)
    
visited = [False for i in range(V)]
dist = [INF for i in range(V)]


for i in range (E):
    # line = input()
    line = f.readline()     
    x , y , z =  line.split(" ")
    x , y , z = int(x) , int(y) , int(z)
     
    graph[x-1].append({y-1:z})

# print(graph)

visited[start] = True
dist[start] = 0

for j in range(V):
    minValue = INF
    minIndex = -1
    # print(dist)
    # print(visited)
    for i in range(len(graph[start])):
        nextVertex = list(list(graph[start])[i].items())[0][0]
        nextValue = list(list(graph[start])[i].items())[0][1]
        if visited[nextVertex]== False:
            if dist[nextVertex] == INF :
                dist[nextVertex] = dist[start] + nextValue
            else:
                if(dist[start]+nextValue<dist[nextVertex]):
                    dist[nextVertex] = dist[start] + nextValue
                    minValue = dist[nextVertex]
                    minIndex = nextVertex
            if (minValue==INF):
                minValue = dist[nextVertex] 
                minIndex = nextVertex
    if minIndex != -1:     
        visited[minIndex] = True
        start = minIndex
        
        
for i in range(len(dist)):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
# print(visited)
# print(dist)

    
    
# f.close()


  
