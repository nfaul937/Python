import sys

def sum(a , c):
    sum = 0
    for i in range(0,len(a)):
        sum += float(a[i][0]) * float(a[i][1])
    
    return (sum * c) 

c = input()
l = input()
a = [None] * int(l)
for i in range(0,int(l)):
    a[i] = input().split()


print(sum(a, float(c)))