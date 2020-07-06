# f = open("input.txt", 'r')
# line = f.readline()
line = input()
num = int(line)

array = []

for i in range(num):
    # line = f.readline()
    line = input()
    array.append(int(line))

def mergeSort(list): 
    if(len(list)<=1):
        return list
    mid = len(list)//2
    leftList = list[0:mid]
    rightList = list[mid:len(list)]
    leftList=mergeSort(leftList)
    rightList=mergeSort(rightList)
    return merge(leftList,rightList)
    
def merge(left,right):
    
    mergedList =[]
    
    while len(left) != 0 or len(right) != 0:
        if len(left) == 0:
            mergedList.append(right[0])
            right.pop(0)
        elif len(right) == 0:
            mergedList.append(left[0])
            left.pop(0)    
        elif(left[0]>right[0]):
            mergedList.append(right[0])
            right.pop(0)
        else: 
            mergedList.append(left[0])
            left.pop(0)    
    return mergedList
    
       
array=mergeSort(array)
for i in range(num):
    print(array[i])
