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

print(graph)

visited[start] = True
dist[start] = 0


for j in range(V):
    minValue = INF
    minIndex = -1
    for i in range(len(graph[start])):
        if visited[i]== False and list(graph[start])[i] != INF:
            if dist[i] == INF :
                dist[i] = dist[start] + graph[start][i]
            else:
                dist[i] = min(dist[start] + graph[start][i],dist[i])
            if (minValue==INF):
                minValue = dist[i] 
                minIndex = i      
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


  
