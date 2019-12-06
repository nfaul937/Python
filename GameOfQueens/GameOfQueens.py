'''
File: gameOfQueens.py
Program author(s): Nick Faul
ClassName: Analysis of Algorithims
Assignment: Game of Queens
Due date: 12/05/2019

Brief description: 
This program reads in a number of queens and uses it as the dimensions for the chessboard. The program will then take the board values in sequence as input.
Once the inputs has been received the program will use patterns to determine the maximum number of queens that can fit on a board.
The program will total the board values that are "under" the queens on the board and return it as output. 
'''
#Swaps values at index i and j in a given array
def swap(arr, i, j):
		arr[i], arr[j] = arr[j], arr[i]

#Find the total value from the board based on the locations given.
def total(board, locations):
    num = 0

    for i in range(0 , len(locations)):
    
        num += int(board[i][locations[i] -1])

    return num

#A function to create a board of size "q x q" where q is the number of queens from the input
#Used in testing only
def makeBoard(q):
    count = 1
    
    for i in range(0,queens):
        for j in range(0, queens):
            board[j][i] = count
            count += 1

queens = int(input())
board = [[None for i in range(queens)] for j in range(queens)]

locations = []
#makeBoard(queens)

#Take the board values as input and place them in the board array
for i in range(queens):
    line = input().split()
    for j in range(queens):
        board[j][i] = line[j]

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

print(total(board, locations))
