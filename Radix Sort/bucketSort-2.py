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
    n = len(arr)

    buckets = [[] for _ in range(n)]

    for i in range(0,n):
       buckets[math.floor(n * arr[i])].insert(0,arr[i])
    
    for i in range(0,n):
        iSort(buckets[i])

    result = []
    for i in range(n):
        
        result.extend(buckets[i])

    return result

arr = [random.uniform(0,1) for j in range(10)]

ans = bucketSort(arr)
print(ans)