def countSort (arr,d):
    #Initialize counting array
    count = [0 for i in range(0,int(max(arr))+1)]
    outArray = [None for i in range(0, len(arr))]

    for j in range(0, len(arr)):
        count[int(arr[j][d])] = count[int(arr[j][d])] + 1

    for i in range(1,max(arr)+1):
        count[i] = count[i] + count[i-1]
        #print(count)

    for j in range(len(arr)-1, -1,-1):
        outArray[count[arr[j][d]] -1 ] = arr[j]
        count[arr[j][d]] = count[arr[j][d]] -1
    
    return outArray

def radixSort (arr, d):

    strArr = [ str(_) for _ in arr ]

    for i in range(0, d):
        print(i)
        countSort(strArr,i)





array = [3,6,3,8,3,1,8,2,1]
ans = radixSort(array, 1)
#print(ans)