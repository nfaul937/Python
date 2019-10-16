import time
import random

def countSort (arr):
    #Initialize counting array
    count = [0 for i in range(0,max(arr)+1)]
    #Initialize array to be returned by function
    outArray = [None for i in range(0, len(arr))]

    #Counting occurance in arr[] and incrementing in count[]
    for j in range(0, len(arr)):
        count[arr[j]] = count[arr[j]] + 1

    #Establishing a running total in count[]
    for i in range(1,max(arr)+1):
        count[i] = count[i] + count[i-1]

    #Placing arr values in correct positions in outArray[]
    for j in range(len(arr)-1, -1,-1):
        outArray[count[arr[j]] -1 ] = arr[j]
        count[arr[j]] = count[arr[j]] -1
    
    return outArray

array =  [random.randint(100000,999999) for j in range(1000000)]
start = time.time()
ans = countSort(array)
end = time.time()
print(end - start)
