x = input()
list = []
for i in range(int(x)):
    list.append(input())
for i in range(int(x)):
    
    if list[i] == 'P=NP':
        print('skipped')
    else:
        a,b = list[i].split('+')
        print(int(a) + int(b))