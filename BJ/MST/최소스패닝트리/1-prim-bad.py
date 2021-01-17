# f = open("input.txt", 'r')
import heapq

edges = []

line = input()
N , M = line.split(" ")
N , M = int(N), int(M)

for j in range(M):
    line = input()
    a , b, c = line.split(" ")
    a , b, c = int(a), int(b) , int(c)
    edges.append([a-1,b-1,c])
        
mst = []
visited = [False] * N
visited[0] = True

pq = []

for edge in edges:
    if edge[0] == 0 or edge[1] == 0: 
        heapq.heappush(pq,(edge[2],edge))
 
answer = 0
    
while pq:
    current = heapq.heappop(pq)[1]
    if visited[current[0]] == False:
        visited[current[0]] = True 
        answer += current[2]
        for edge in edges:
            if edge[0] == current[0] or edge[1] == current[0]: 
                heapq.heappush(pq,(edge[2],edge))
    elif visited[current[1]] == False:
        visited[current[1]] = True  
        answer += current[2]
        for edge in edges:
            if edge[0] == current[1] or edge[1] == current[1]: 
                heapq.heappush(pq,(edge[2],edge))
    
print(answer)


