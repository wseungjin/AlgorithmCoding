from collections import defaultdict

line = input()
n = int(line)

line = input()
m = int(line)

INF = 10000000

graph = [[INF for i in range(n)] for j in range(n)]



for i in range(m):
    line = input()
    x , y , z =  line.split(" ")
    x , y , z = int(x) - 1 , int(y) - 1, int(z)
    graph[x][y] = min(graph[x][y],z)
    
for mid in range(n):
    for start in range(n):
        for end in range(n):
            if start != mid and mid != end and start !=end:
                graph[start][end] = min(graph[start][end], graph[start][mid]+graph[mid][end])

for start in range(n):
    for end in range(n):
        if graph[start][end] == INF : graph[start][end] = 0
        print(graph[start][end],end = " ")
    print("")

    
    
# f.close()


  
