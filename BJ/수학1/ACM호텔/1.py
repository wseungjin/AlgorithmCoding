# f = open("input.txt", 'r')
# testNum = int(f.readline())
testNum = int(input())

for t in range (testNum):
    
    line = input()
    # line= f.readline()
    output=line.split(" ")
    h=int(output[0])
    w=int(output[1])
    n=int(output[2])
    
    second=n//h+1
    first=n%h
    
    if(first==0):
        first=h
        second=second-1
        
    
    if(second<10):
        second="0"+str(second)
    
    print(first,end='')
    print(second)

# f.close()