
# f = open("input.txt", 'r')

array = [[0 for i in range(9)] for j in range(9)]
route = [] 
routeNum = 0
visited = [[True for i in range(9)] for j in range(9)]

flag = False

for i in range(9):
    line = input()
    # line = f.readline()
    line = line.replace("\n","")
    for j in range(9):
        array[i][j]=int(line.split(" ")[j])
        if(array[i][j] == 0):
            visited[i][j] = False
            routeNum = routeNum + 1
            route.append([i,j,0])
    
def DFS(count):
    global flag
    # 완료했을경우 바로 탈출
    if flag == True :
        return
    # 만족하지 못한경우
    if count !=0:
        I = route[count-1][0] 
        J = route[count-1][1] 
        #세로가 같은경우
        for i in range(9):
            if array[i][J]==array[I][J] and i!=I :
                return
        #가로가 같은경우
        for j in range(9):
            if array[I][j]==array[I][J] and j!=J :
                return
        districtI=I//3
        districtJ=J//3
        #같은 구역에서 같은 숫자가 있을 경우
        for i in range(3*districtI,3*districtI+3):
            for j in range(3*districtJ,3*districtJ+3):
                if(array[i][j]==array[I][J] and (i!=I and j!=J)):
                    return

    # 전부 만족한경우
    if(count == routeNum):
        for i in range(9):
            for j in range(9):
                print(array[i][j], end=" ")
            print("")
        flag = True
        return
    
    for i in range(1,10):
        I = route[count][0] 
        J = route[count][1] 
        route[count][2] = i
        array[I][J] = i
        DFS(count+1)
        array[I][J] = 0
        route[count][2] = 0

            
DFS(0)
