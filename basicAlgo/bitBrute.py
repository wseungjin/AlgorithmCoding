array = []

n = 4
for i in range(1<<n):
    bit = i
    j = 0
    string = [0] * n
    while bit !=0:
        if ((1 & bit) != 0):
            string[n-1-j] = 1
        j += 1
        bit = bit >> 1
        
    array.append(string)
    
print(array)