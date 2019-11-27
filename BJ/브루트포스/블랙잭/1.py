# f = open("input.txt", 'r')
# line = f.readline()
line = input()


output=line.split(" ")

N=int(output[0])
M=int(output[1])

# line = f.readline()
line = input()

near = 0 
output=line.split(" ")
current=0
for i in range(N):
    
    for j in range(N):
        
        for k in range(N):
            
            if(i==j or j==k or i==k):
                continue
            else:
                current=int(output[i])+int(output[j])+int(output[k])
                if(near<current and current<=M):
                    near=current
                

print(near)