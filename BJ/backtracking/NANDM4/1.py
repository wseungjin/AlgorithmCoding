# f = open("input.txt", 'r')
# line = f.readline()
line = input()

output=line.split(" ")

N=int(output[0])
M=int(output[1])

array=[]
visited = [False] * N
route =[]

for i in range(N):
    array.append(i+1) 
    
def printRoute(route):
    for i in range(len(route)):
        print(route[i],end= " ")
    print("")
    
def DFS(count):
    if(len(route)>1 and route[len(route)-1]<route[len(route)-2]):
        return
    if(count>=M):
        printRoute(route)
        return 
    for i in range(N):
        route.append(array[i])
        DFS(count+1)
        route.pop()   
            
DFS(0)