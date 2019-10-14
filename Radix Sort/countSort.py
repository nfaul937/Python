def countSort (arr):
    #Initialize counting array
    count = [0 for i in range(0,max(arr)+1)]
    outArray = [None for i in range(0, len(arr))]

    for j in range(0, len(arr)):
        count[arr[j]] = count[arr[j]] + 1

    for i in range(1,max(arr)+1):
        count[i] = count[i] + count[i-1]
        #print(count)

    for j in range(len(arr)-1, -1,-1):
        outArray[count[arr[j]] -1 ] = arr[j]
        count[arr[j]] = count[arr[j]] -1
    
    return outArray

array = [3,6,3,8,3,1,8,2,10]
ans = countSort(array)
print(ans)
