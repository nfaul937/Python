
import time
import random
import math

def iSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp

def setGroups(arr):
    size = 5
    groups = [arr[i:i+size] for i  in range(0, len(arr), size)]
    return groups

def medianOfFive(arr):
    groups = []
    groups = setGroups(arr)

    for i in range(0,len(groups)):
        iSort(groups[i])
    
    medians = []
    print (groups)
    for i in range(0,len(groups)):
        medianindex = math.ceil(int(len(groups[i])/2))
        medians.append(groups[i][int(medianindex)])
    return medians


array =  [random.randint(1,100) for j in range(7)]

start = time.time()

sortedgroups = medianOfFive(array)
print(sortedgroups)
end = time.time()