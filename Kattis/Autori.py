x = input()

a = x.split('-')
b = ''
for i in range(0,len(a)):
     b += a[i][0]
print(b)