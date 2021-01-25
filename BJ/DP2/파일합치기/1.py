
testCase = input()
testCase=int(testCase)

answer = []

for _ in range(testCase):
    n = input()
    n=int(n)
    
    line = input()
    split_data = line.split(' ')
    data = list(map(int,split_data))
    
    INF = 257 * 500 * 10000
    m = [[INF for i in range(n)] for j in range(n)] 
    s = [[INF for i in range(n)] for j in range(n)] 

    for i, num in enumerate(data):
        m[i][i] = num
        s[i][i] = num
        
    for startX in range(1,n):
        tarX = startX
        tarY = startX - 1
        
        length = 1
        while tarY > -1:
            s[tarY][tarX] = s[tarY+1][tarX] + s[tarY][tarX - length] 
            tarY -= 1
            length += 1
        
    for length in range(1,n):
        for start in range(0,n-length):
            end = start + length
            
            finalY = start
            finalX = end
                        
            for index in range(length):
                firstY = start
                firstX = start + index
                
                secondY = start + 1 + index
                secondX = end

                value = s[finalY][finalX]
                add1 = m[firstY][firstX]
                add2 = m[secondY][secondX]
                if firstX == firstY:
                    add1 = 0
                if secondX == secondY:
                    add2 = 0
                m[finalY][finalX] = min(m[finalY][finalX], value + add1 + add2)
    answer.append(m[0][n-1])
for ans in answer:
    print(ans)