import math
# f = open("input.txt", 'r')
# line = f.readline()
line = input()


output=line.split(" ")

a=int(output[0])
b=int(output[1])
v=int(output[2])

# if(v>a):
temp = v-a
temp = math.ceil(temp/(a-b)) 
temp = temp + 1 
# else:
#     temp=1
print(temp)