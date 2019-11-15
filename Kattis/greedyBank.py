import numbers

num, tlimit = input().split()

def sortThird(val): 
    return val[2] 

a = [[None for i in range(3)] for j in range(int(num))]
minDeposit = [None] * int(num)
sum = 0

for i in range(0,int(num)):
    deposit , maxWait= input().split()
    a[i][0] = deposit
    a[i][1] = maxWait
    if int(maxWait) == 0:
        a[i][2] = int(deposit)
    else:
        a[i][2] = int(deposit)/int(maxWait)

a.sort(key = sortThird, reverse = True)

