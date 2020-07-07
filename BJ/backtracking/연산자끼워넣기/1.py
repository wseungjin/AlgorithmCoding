# f = open("input.txt", 'r')
# line = f.readline()
line = input()

N=int(line)

array = []
route = []
line = input()
line = line.replace("\n","")
output=line.split(" ")

for i in range(N):
    array.append(int(output[i]))

operator = []
operatorNum = N-1
line = input()
line = line.replace("\n","")
for i in range(4):
    operator.append(int(line.split(" ")[i]))
    
glomin = 1000000000
glomax = -1000000000

def cal():
    result = array[0]
    for i in range(operatorNum):
        if route[i] == 0:
            result = result + array[i+1]
        elif route[i] == 1:
            result = result - array[i+1]
        elif route[i] == 2:
            result = result * array[i+1]
        elif route[i] == 3:
            if result <0 :
                result = (-result) // array[i+1]
                result = - result
            else:
                result = result // array[i+1]
    return result
    
def DFS(count):
    global glomax  
    global glomin 
    if(count==operatorNum):
        result=cal()
        if(result>glomax):
            glomax = result
        if(result<glomin):
            glomin = result
        return
    for i in range(4):
        if(operator[i]>0):
            operator[i] = operator[i] - 1
            route.append(i)
            DFS(count+1)
            operator[i] = operator[i] + 1
            route.pop()
DFS(0)

print(glomax)
print(glomin)