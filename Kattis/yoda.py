
def initArray(array, string):
    for i in range(len(string)):
        if string[i]:
            array[i] = string[i]
        else:
            break

def ArrayToInt(array):
    num = ""
    for i in range(len(array)):
        if array[i] == None:
            continue
        else:
            num += array[i]
    if num == "":
        num = 'YODA'
    elif int(num) == 0:
        num = 0
    return num

x = input()
y = input() 
length = max(len(x), len(y))
xArray = [None] * length
yArray = [None] * length

initArray(xArray,x)
initArray(yArray,y)

for i in range(length):
    if xArray[i] == None or yArray[i] == None:
        continue
    if xArray[i] < yArray[i]:
        xArray[i] = None
    elif yArray[i] < xArray[i]:
        yArray[i] = None
    else:
        continue


print(ArrayToInt(xArray))
print(ArrayToInt(yArray))