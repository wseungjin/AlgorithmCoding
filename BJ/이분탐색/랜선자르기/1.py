from collections import defaultdict

def binSearch(array,wanted,left,right):
    mid = (left + right) // 2
    
    if left > right:
        return right
    
    sumValue = 0
    
    for arrayValue in array:
        sumValue += arrayValue//mid  
                
    if sumValue >= wanted:
        return binSearch(array,wanted,mid+1,right)
    else: 
        return binSearch(array,wanted,left,mid-1)
    
    


# f = open("input.txt", 'r')

# line = f.readline()
line = input()

K , N = line.split(" ")
K , N = int(K), int(N)

array = []

for i in range(K):
    # line = f.readline()
    line = input()
    array.append(int(line))

print(binSearch(array,N,0,pow(2,31)-1))
    