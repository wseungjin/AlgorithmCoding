# f = open("input.txt", 'r')
# line = f.readline()

line = input()
# line = f.readline()

line = line.replace("\n","")
N=int(line)


array = [[0 for i in range(N)] for j in range(N)]

whiteNum = 0
blueNum = 0


for i in range(N):
    line = input()
    # line = f.readline()
    line = line.replace("\n","")
    for j in range(N):
        array[i][j]= int(line.split(" ")[j])


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
        newSize = int(size/2)
        reccurence(newSize,x,y) 
        reccurence(newSize,x+newSize,y) 
        reccurence(newSize,x,y+newSize) 
        reccurence(newSize,x+newSize,y+newSize)   
    else: 
        if value == 0:
            whiteNum = whiteNum + 1
        else:
            blueNum = blueNum + 1
        return
    
    
    
reccurence(N,0,0)

print(whiteNum)
print(blueNum)