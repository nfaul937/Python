import time
import random

def RadCountSort (arr,d):
    #Initialize counting array
    count = [0 for i in range(0,10)]
    
    outArray = [None for i in range(0, len(arr))]

    for j in range(0, len(arr)):
        count[int(arr[j][d])] = count[int(arr[j][d])] + 1

    for i in range(1,10):
        count[i] = count[i] + count[i-1]
        #print(count)

    for j in range(len(arr)-1, -1,-1):
        outArray[count[int(arr[j][d])] -1 ] = int(arr[j])
        count[int(arr[j][d])] = count[int(arr[j][d])] -1
    
    return outArray

def radixSort (arr, d):

    strArr = [ str(_) for _ in arr ]

    for i in range(d-1, -1, -1):
        print(i)
        sortedArray = RadCountSort(strArr,i)
        strArr = [ str(_) for _ in sortedArray ]
    
    return sortedArray

array = [random.randint(10,99) for j in range(20)]
ans = radixSort(array, 2)
print(ans)