
queens = int(input())

board = [[None for i in range(queens)] for j in range(queens)]


for i in range(queens):
    line = input().split()
    for j in range(queens):
        board[j][i] = line[j]
    

