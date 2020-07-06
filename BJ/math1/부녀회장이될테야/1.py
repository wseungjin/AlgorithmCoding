# f = open("input.txt", 'r')
# testNum = int(f.readline())
testNum = int(input())


house = [[0]*15 for i in range(15)]

# print(house)

for y in range(15):
    for x in range(15):
        if(y==0):
            house[y][x]=x+1

        else:
            if(x==0):
                house[y][x]=house[y-1][x]
            else: 
                house[y][x]=house[y-1][x]+house[y][x-1]

# testNum = input()

for t in range (testNum):
    k = int(input())
    # k= int(f.readline())
    n = int(input())
    # n= int(f.readline())      
    print(house[k][n-1])
# print(house)     
# f.close()