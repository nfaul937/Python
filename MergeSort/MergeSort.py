import time
import random
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        leftArray = arr[:mid] # Dividing the array elements  
        rightArray = arr[mid:] # into 2 halves 
  
        mergeSort(leftArray) # Sorting the first half 
        mergeSort(rightArray) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(leftArray) and j < len(rightArray): 
            if leftArray[i] < rightArray[j]: 
                arr[k] = leftArray[i] 
                i+=1
            else: 
                arr[k] = rightArray[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(leftArray): 
            arr[k] = leftArray[i] 
            i+=1
            k+=1
          
        while j < len(rightArray): 
            arr[k] = rightArray[j] 
            j+=1
            k+=1

x = 1
for i in range(1000000,1300001,50000):
    
    arr =  [random.randint(0,100000) for j in range(i)]
    
    start = time.time()
    mergeSort(arr)
    end = time.time()
    print()
    print("Round " + str(x))
    print(len(arr))
    print(end - start)
    x += 1