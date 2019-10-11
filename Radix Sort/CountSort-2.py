def countSort (arr):
    #Initialize counting array
    count = [0 for i in range(0,max(arr)+1)]

    for j in range(0, len(arr)):
        count[arr[j]] = count[arr[j]] + 1
        print(count)

array = [3,6,3,8,3,1,8,2,10]
countSort(array)