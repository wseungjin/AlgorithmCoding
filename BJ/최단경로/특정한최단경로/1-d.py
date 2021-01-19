import heapq

line = input()
V , E = line.split(" ")
V , E= int(V) , int(E)

INF = 800 * 1000
graph = [[] for _ in range(V)]
for _ in range(E):
    v1, v2, cost = map(int, input().split())
    graph[v1 - 1].append((v2 - 1, cost))
    graph[v2 - 1].append((v1 - 1, cost))
    
line = input()
v1 , v2 = line.split(" ")
v1 , v2 = int(v1) -1 , int(v2) -1

pq = []
distFrom0 = [INF] * V
heapq.heappush(pq, (0, 0))
distFrom0[0] = 0

while pq:
    distHere, here = heapq.heappop(pq)
    if distHere > distFrom0[here]:
        continue
    for there, distThere in graph[here]:
        distThere += distHere
        if distThere < distFrom0[there]:
            heapq.heappush(pq, (distThere, there))
            distFrom0[there] = distThere

pq = []
distFromV1 = [INF] * V
heapq.heappush(pq, (0, v1))
distFromV1[v1] = 0

while pq:
    distHere, here = heapq.heappop(pq)
    if distHere > distFromV1[here]:
        continue
    for there, distThere in graph[here]:
        distThere += distHere
        if distThere < distFromV1[there]:
            heapq.heappush(pq, (distThere, there))
            distFromV1[there] = distThere
            
pq = []
distFromV2 = [INF] * V
heapq.heappush(pq, (0, v2))
distFromV2[v2] = 0

while pq:
    distHere, here = heapq.heappop(pq)
    if distHere > distFromV2[here]:
        continue
    for there, distThere in graph[here]:
        distThere += distHere
        if distThere < distFromV2[there]:
            heapq.heappush(pq, (distThere, there))
            distFromV2[there] = distThere

answer = min(distFrom0[v1] + distFromV1[v2] + distFromV2[V-1],distFrom0[v2] + distFromV2[v1] + distFromV1[V-1])

if answer >= INF:
    answer = -1
print(answer)

    

  
