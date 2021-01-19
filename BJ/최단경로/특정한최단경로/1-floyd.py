line = input()
V , E = line.split(" ")
V , E= int(V) , int(E)

INF = 800 * 1000

graph = [[INF for i in range(V)] for j in range(V)]

for i in range(E):
    line = input()
    x , y , z =  line.split(" ")
    x , y , z = int(x) - 1 , int(y) - 1, int(z)
    graph[x][y] = min(graph[x][y],z)
    graph[y][x] = min(graph[y][x],z)
    
line = input()
v1 , v2 = line.split(" ")
v1 , v2 = int(v1) -1 , int(v2) -1

for mid in range(V):
    for start in range(V):
        for end in range(V):
            if start != mid and mid != end and start !=end:
                graph[start][end] = min(graph[start][end], graph[start][mid]+graph[mid][end])

answer = min(graph[0][v1] + graph[v1][v2] + graph[v2][V-1],graph[0][v2] + graph[v2][v1] + graph[v2][V-1])

if answer >= INF:
    answer = -1
print(answer)

    

  
