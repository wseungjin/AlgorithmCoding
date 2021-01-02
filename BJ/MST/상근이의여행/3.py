import sys

input = sys.stdin.readline

line = input()
testCase = int(line)

NArray = []
for i in range(testCase):
    line = input()
    N , M = line.split(" ")
    N , M = int(N), int(M)
    NArray.append(N)
        
    for j in range(M):
        line = input()
        a , b = line.split(" ")
        a , b = int(a), int(b)
  

for N in NArray:
    print(N-1)

