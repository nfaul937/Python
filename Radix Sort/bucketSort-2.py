import math
import random
import time

def iSort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp

def bucketSort(arr):
    #Get and store length of array
    n = len(arr)

    #Initilize buckets array as a list of lists for 
    buckets = [[] for _ in range(n)]

    #Insert value of arr[i] at the location specified in the buckets array
    for i in range(0,n):
        buckets[int(math.floor(n * arr[i]))].insert(0,arr[i])
    
    #Sort each list in the list of buckets using insertion sort
    for i in range(0,n):
        iSort(buckets[i])

    #Initilize result as an empty list
    result = []

    #Append each list in bucket to the result list
    for i in range(n):
        result.extend(buckets[i])

    return result

arr = [random.uniform(0,1) for j in range(1000000)]
start = time.time()
bucketSort(arr)
end = time.time()
print(end - start)