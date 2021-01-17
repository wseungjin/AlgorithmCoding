# f = open("input.txt", 'r')
import heapq

edges = []

line = input()
N , M = line.split(" ")
N , M = int(N), int(M)

INF = 1000001    

graph = [[INF for i in range(N)] for j in range(N)]

for i in range(N):
    graph[i][i] = 0

for i in range(M):
    line = input()
    a , b, c = line.split(" ")
    a , b, c = int(a), int(b) , int(c)
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

def getMinIndex(dist,visited):
    minIndex = -1
    minValue = INF
    
    for i in range(len(dist)):
        if visited[i] == False and minValue>dist[i]:
            minValue = dist[i]
            minIndex = i
    return minIndex
 
def prim(N,graph):
    
    dist = [INF] * N
    visited = [False] * N            
    dist[0] = 0       
    
    for i in range(N):
        minIndex = getMinIndex(dist,visited)
        visited[minIndex] = True
        for j in range(N):
            if graph[minIndex][j] < dist[j] and visited[j] == False:
                dist[j] = graph[minIndex][j]
            
    answer = 0
    for i in range(N):
        answer += dist[i]
    print(answer)


prim(N,graph)
