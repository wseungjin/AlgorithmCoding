import sys
import heapq

INF = 987654321
input = sys.stdin.readline
# print = sys.stdout.write

vertex, edge = map(int, input().split())
start = int(input())
graph = [[] for _ in range(vertex + 1)]
for _ in range(edge):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))
    
    
# print(graph)

pq = []
dist = [INF] * (vertex + 1)
heapq.heappush(pq, (0, start))
dist[start] = 0

# print(pq)

while pq:
    # print(pq)
    distHere, here = heapq.heappop(pq)
    if distHere > dist[here]:
        continue
    for there, distThere in graph[here]:
        distThere += distHere
        if distThere < dist[there]:
            heapq.heappush(pq, (distThere, there))
            dist[there] = distThere

for i in range(1, vertex + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])