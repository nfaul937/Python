
def countSort(arr): 
    
    output = [0 for i in range(256)] 
    
    count = [0 for i in range(256)] 
  
    ans = ["" for _ in arr] 
   
    for i in arr: 
        count[i] += 1
  
    
    for i in range(256): 
        count[i] += count[i-1] 
  
   
    for i in range(len(arr)): 
        output[count[arr[i]]-1] = arr[i] 
        count[arr[i]] -= 1
  
    
    for i in range(len(arr)): 
        ans[i] = output[i] 
    return ans  

arr = [1,2,3,4,7,2,9,65,3]
ans = countSort(arr) 
print(ans[1])
print(type(ans[1]))
print(ans)