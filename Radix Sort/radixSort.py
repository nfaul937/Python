def RadCountSort (arr,d):
    #Initialize counting array
    count = [0 for i in range(0,10)]
    
    outArray = [None for i in range(0, len(arr))]

    for j in range(0, len(arr)):
        count[int(arr[j][d])] = count[int(arr[j][d])] + 1

    for i in range(1,int(len(arr))+1):
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



array = [3223,1634,2345,4962,5371,6162,7803,8270,9105]
ans = radixSort(array, 4)
print(ans)