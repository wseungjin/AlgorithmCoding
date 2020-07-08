# f = open("input.txt", 'r')
# line = f.readline()

line = input()
# line = f.readline()

line = line.replace("\n","")
N=int(line)


array = [[0 for i in range(N)] for j in range(N)]


for i in range(N):
    line = input()
    # line = f.readline()
    for j in range(N):
        array[i][j]= int(line[j])


def reccurence(size,x,y):
    global whiteNum
    global blueNum
    value = array[x][y]
    flag = True
    for i in range(x,x+size):
        if flag == False :
            break
        for j in range(y,y+size):
            if(array[i][j]!=value):
                flag = False
                break
   
    if flag == False :
        print("(",end="")
        newSize = int(size/2)
        reccurence(newSize,x,y) 
        reccurence(newSize,x,y+newSize) 
        reccurence(newSize,x+newSize,y) 
        reccurence(newSize,x+newSize,y+newSize) 
        print(")",end="")  
    else: 
        if value == 0:
            print(0,end="")
        else:
            print(1,end="")
        return
    
    
    
reccurence(N,0,0)

