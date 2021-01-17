# f = open("input.txt", 'r')
import heapq

edges = {}

line = input()
N , M = line.split(" ")
N , M = int(N), int(M)


for j in range(M):
    line = input()
    a , b, c = line.split(" ")
    a , b, c = int(a), int(b) , int(c)
    try:
        edges[a-1].append((b-1,c))
    except:
        edges[a-1] = [(b-1,c)]
    try:
        edges[b-1].append((a-1,c))
    except:
        edges[b-1] = [(a-1,c)]

    
visited = [False] * N
visited[0] = True
pq = []

for nextTo,weight in edges[0]: 
    heapq.heappush(pq,(weight,(0,nextTo,weight)))
 
answer = 0
 
while pq:
    current = heapq.heappop(pq)[1]
    nextIndex = current[1]
    if visited[nextIndex] == False:
        visited[nextIndex] = True
        answer += current[2]
        
        for nextTo,weight in edges[nextIndex]: 
            if visited[nextTo] == False:
                heapq.heappush(pq,(weight,(nextIndex,nextTo,weight)))
    
print(answer)


