# f = open("input.txt", 'r')
# line = f.readline()

line = input()
# line = f.readline()

line = line.replace("\n"," ")
N=int(line)


array = [0] * N

inc = [0] * N
dec = [0] * N


line = input()
# line = f.readline()
line = line.replace("\n"," ")

for i in range(N):
    array[i]= int(line.split(" ")[i])

inc[0] = 1
dec[N-1] = 1

for incIndex in range(1,N):
    maxInc = 0
    maxDec = 0
    decIndex = N - 1 - incIndex
    for j in range(incIndex,-1,-1):
        if array[incIndex]>array[j] and (maxInc==0 or maxInc<inc[j]):    
            maxInc = inc[j]
    for j in range(decIndex,N):
        if array[decIndex]>array[j] and (maxDec==0 or maxDec<dec[j]):    
            maxDec = dec[j]
    inc[incIndex] = maxInc + 1
    dec[decIndex] = maxDec + 1
      
maxValue = 1
for i in range (1,N-1):
    if inc[i] > 1 and dec[i] > 1:
        maxValue = max(maxValue,inc[i]+ dec[i] - 1)
print(maxValue)