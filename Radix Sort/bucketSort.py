import time
import random

def bucketSort(arr):
    largest = max(arr)
    length = len(arr)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    
    for i in range(length):
        j = int(arr[i]/size)
        if j != length:
            buckets[j].append(arr[i])
        else:
            buckets[length - 1].append(arr[i])
 
    for i in range(length):
        iSort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def iSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
 
 
arr = [random.randint(1000,9999) for j in range(10)]
sorted_list = bucketSort(arr)

print('Sorted list: ', end='')
print(sorted_list)