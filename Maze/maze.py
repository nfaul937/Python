
class Node:
    def __init__(self, coord=None, north=None, south=None, east=None, west=None):
        self.coord = coord
        self.north = north
        self.south = south
        self.east = east
        self.west = west

name = input()

row, col, intersect = input().split()
row = int(row)
col = int(col)
intersect = int(intersect)

#Creating a blank maze board of size (row + 1 by col + 1) with an edge of None cells
board = [[None for i in range(row + 1)] for j in range(col + 1)]

#parsing line for starting node, direction, and end
endpoints = input().split()
start = endpoints[0], endpoints[1] 
end = endpoints[3], endpoints[4]
startDir = endpoints[2]
board = [[None for i in range(row + 1)] for j in range(col + 1)]

board[int(start[0])][int(start[1])] = Node(start)

print(board)