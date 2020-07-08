# f = open("input.txt", 'r')
# line = f.readline()
line = input()

N=int(line)

array = []

answer1 = [0] * (N +1)
answer2 = [0] * (N +1)


array.append(0)

for i in range (N):
    # line = f.readline()
    line = input()
    array.append(int(line))
    

for i in range (1,N+1):
    
    if(i==1):
        answer2[i] = array[i]
    else:
        answer1[i] = answer2[i-1] + array[i]
        answer2[i] = max(answer1[i-2],answer2[i-2]) + array[i]
    
print(max(answer1[N],answer2[N]))

    
    
    
