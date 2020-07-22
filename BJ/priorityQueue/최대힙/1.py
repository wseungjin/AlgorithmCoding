import sys
import heapq

N=int(input())

pq = []

answer = []
for i in range(N):
    x=int(input())
    if x==0:
        if pq:
            output=heapq.heappop(pq)[1]
            answer.append(output)
        else:
            answer.append(0)
    else:
        heapq.heappush(pq,(-x,x))
    
    
for i in range(len(answer)):
    print(answer[i])