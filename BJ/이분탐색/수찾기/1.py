from collections import defaultdict

def binSearch(array,wanted,left,right):
    mid = (left + right) // 2
    
    if left > right:
        return False
    
    if array[mid] == wanted:
        return True
    
    if array[mid] > wanted:
        return binSearch(array,wanted,left,mid-1)
    else: 
        return binSearch(array,wanted,mid+1,right)
    
    


# f = open("input.txt", 'r')

# line = f.readline()
line = input()

N = int(line)

# line = f.readline()
line = input()

A = list(map(int,line.split(" ")))

# line = f.readline()
line = input()

M = int(line)

# line = f.readline()
line = input()

B = list(map(int,line.split(" ")))

A = sorted(A)

for findNum in B:
    isFound = binSearch(A,findNum,0,len(A)-1)
    if isFound:
        print("1")
    else: 
        print("0")