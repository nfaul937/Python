def initBlockList(numOfBlocks):
    mdarray = [[None for i in range(numOfBlocks)] for j in range(numOfBlocks)]
    for i in range(numOfBlocks):
        mdarray[i][0] = i
    return mdarray

def findBlock(target, array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == target:
                print("target found")
                row = j
                col = i
                break
        if array[i][j] == target:
                break
    return row, col

def returnBlocks(target, array):
    row, col = findBlock(target, array)
    limit = len(array) - (len(array) - row - 1)

    for i  in range(limit,len(array)):
        value = array[col][i]
        if value == None:
            continue
        array[col][i] = None
        array[value][0] = value
    return mdarray
    
def moveOnto(src, dst, array):
    returnBlocks(src,array)
    returnBlocks(dst, array)
    dstRow,dstCol = findBlock(dst,array)
    srcRow,srcCol = findBlock(src,array)
    value = array[srcCol][srcRow]
    array[dstCol][dstRow + 1] = value
    array[srcCol][srcRow] = None
    return

def moveOver(src, dst, array):
    returnBlocks(src,array)
    dstRow,dstCol = findBlock(dst,array)
    srcRow,srcCol = findBlock(src,array)
    value = array[srcCol][srcRow]

    for i in range(len(array)):
        if array[dstCol][i] == None:
            array[dstCol][i] = value
            array[srcCol][srcRow] = None
            break
    return
mdarray = initBlockList(10)

mdarray[1][1] = 9
mdarray[1][2] = 2
mdarray[1][3] = 4
mdarray[2][0] = None
mdarray[4][0] = None
mdarray[5][1] = 8
mdarray[5][2] = 7
mdarray[5][3] = 6
mdarray[6][0] = None
mdarray[7][0] = None
mdarray[8][0] = None
mdarray[9][0] = None


returnBlocks(5, mdarray)

moveOnto(3, 0, mdarray)
returnBlocks(0, mdarray)
moveOnto(5, 3, mdarray)
print()
print("The following array should match the array form the test output")
print(mdarray)





