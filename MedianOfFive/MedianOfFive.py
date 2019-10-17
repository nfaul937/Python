
import time
import random
import math

def setGroups(arr):
    
    size = 5
    groups = [arr[i:i+size] for i  in range(0, len(arr), size)]

    return groups

#def medianOfFive(arr):



array =  [random.randint(0,20) for j in range(11)]

start = time.time()
ans = setGroups(array)
print(ans)
end = time.time()