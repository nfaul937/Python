'''
File: blockProblem.py
Program author(s): Nick Faul
ClassName: Analysis of Algorithims
Assignment: Low Hanging Fruit - Assignment #0
Due date: 09/03/2019

Brief description: 
This program reads input from a text file name "blocksIn.txt" that is located in the working directory. The program reads each line from the file a interprets the command. Based on the command given, the program will use the corresponding from the assignment. Once a quit command is parsed from the input file, the program will then write the results to a file called "blocksOut.txt"
'''
import sys

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
    return array

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
    
inputFile = open("blocksTestIn.txt", "r")

#Read line from inout file and strip white space/ new line characters
cmdline = (inputFile.readline()).rstrip()

#Set total number on blocks in problem and cast type to integer.
numOfBlocks = int(cmdline)

#Initialize the array with requireed number of blocks
array = initBlockList(numOfBlocks)

'''
while True:
    cmdline = (inputFile.readline()).rstrip()

    phrase = cmdline.split()
    if len(phrase) == 4:
        action = phrase[0]
        subaction = phrase[2]
        source = phrase[1]
        dest = phrase[3]
    else:
        action = phrase
        if action[0] == "quit":
            sys.exit()
    
    if action != "move" and action != "pile":
        print ("invalid command found in file")

    elif action == "move" and subaction == "over":
        print ("move over")
        
    elif action == "move" and subaction == "onto":
        print ("move onto")
        
    elif action == "pile" and subaction == "over":
        print ("pile over")

    elif action == "pile" and subaction == "onto":
        print ("pile onto")
 '''   

        