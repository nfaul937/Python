import time
import random

def RadCountSort (arr,d):
    #Initialize counting array
    count = [0 for i in range(0,10)]
    
    #Initialize array to be returned by function
    outArray = [None for i in range(0, len(arr))]

    #Counting occurance in arr[] and incrementing in count[]
    for j in range(0, len(arr)):
        count[int(arr[j][d])] = count[int(arr[j][d])] + 1

    #Establishing a running total in count[]
    for i in range(1,10):
        count[i] = count[i] + count[i-1]

    #Placing arr values in correct positions in outArray[]
    for j in range(len(arr)-1, -1,-1):
        outArray[count[int(arr[j][d])] -1 ] = int(arr[j])
        count[int(arr[j][d])] = count[int(arr[j][d])] -1
    
    return outArray

def radixSort (arr, d):

    #Initialize string array to be used by function
    strArr = [ str(_) for _ in arr ]

    #Decrement through digit values and sort with RadCountSort
    for i in range(d-1, -1, -1):

        #Sorting strArr and storing in sortedArray variable
        sortedArray = RadCountSort(strArr,i)

        #Casting sortedArray as strings for next iteration
        strArr = [ str(_) for _ in sortedArray ]
        
    return sortedArray

array =  [random.randint(100000,999999) for j in range(100000)]
start = time.time()
ans = radixSort(array,6)
end = time.time()
print(end - start)