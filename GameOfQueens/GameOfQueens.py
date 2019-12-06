
def swap(arr, i, j):
		arr[i], arr[j] = arr[j], arr[i]

def total(board, locations):
    num = 0

    for i in range(0 , len(locations)):
        num += board[i][locations[i] -1]

    return num

def makeBoard(q):
    count = 1
    
    for i in range(0,queens):
        for j in range(0, queens):
            board[j][i] = count
            count += 1

queens = int(input())
board = [[None for i in range(queens)] for j in range(queens)]

locations = []
makeBoard(queens)
'''
for i in range(queens):
    line = input().split()
    for j in range(queens):
        board[j][i] = line[j]
   ''' 

mod = queens % 6

if mod == 2:
    for i in range(2, queens + 2, 2):
        locations.append(i)
    for i in range(1 , queens , 2):
        locations.append(i)
    swap(locations, locations.index(1), locations.index(3))
    locations.remove(5)
    locations.append(5)

elif mod == 3:
    for i in range(2, queens + 1, 2): 
        locations.append(i)
    for i in range(1 , queens + 1, 2):
        locations.append(i)
    locations.remove(2)
    locations.insert(locations.index(queens - 1) + 1, 2)
    locations.remove(1)
    locations.append(1)
    locations.remove(3)
    locations.append(3)
    
else:
    for i in range(2, queens + 2, 2):
        locations.append(i)
    for i in range(1 , queens , 2):
        locations.append(i)


print(locations)

ans = total(board , locations)
print(ans)