# f = open("input.txt", 'r')
# line = f.readline()
line = input()

N=int(line)

array=[]
route =[]
answer = 0
visited = [False] * N


for i in range(N):
    array.append(i+1) 


def checkRoute():
    flag = True
    routeNum = len(route)
    if (routeNum >1):
        for i in range (routeNum-2,-1,-1):
            if(abs(route[routeNum-1]-route[i])==abs(routeNum-1-i)):
                flag = False
                break
    return flag
    
    
def DFS(count):
    global answer
    if checkRoute()==False:
        return
    if(count==N):
        answer = answer + 1
        return 
    for i in range(N):
        if(visited[i]==False):
            visited[i] = True        
            route.append(array[i])
            DFS(count+1)
            visited[i] = False
            route.pop()   
            
DFS(0)

print(answer)