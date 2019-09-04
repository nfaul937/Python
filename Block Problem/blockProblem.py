'''
File: blockProblem.py
Program author(s): Nick Faul
ClassName: Analysis of Algorithims
Assignment: Low Hanging Fruit - Assignment #0
Due date: 09/03/2019

Brief description: 
This program reads input from a text file name taken from the command line that is located in the working directory. 
The program reads each line from the file a interprets the command. 
Based on the command given, the program will use the corresponding from the assignment. 
Once a quit command is parsed from the input file, the program will then write the results to a file with a name received from the command line.
'''
import sys

#initBlockList: numOfBlocks = the number of blocks from the input file.
#Initialize an array that is m by n with value None, where m and n are the number of starting blocks 
def initBlockList(numOfBlocks):
    mdarray = [[None for i in range(numOfBlocks)] for j in range(numOfBlocks)]
    for i in range(numOfBlocks):
        mdarray[i][0] = i
    return mdarray

#findBlock: target = the integer of the block needed, array = the working array
#A function that takes a finds a target integer in the array. Returns coordinates for the target in the array.
def findBlock(target, array):
    #row, col = [0,0]
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == target:
                row = j
                col = i
                break
        if array[i][j] == target:
                break
    return row, col

#returnBlocks: target = the target block to returns values above, array = the working array
#Returns the row and column values of the target block.
#A function that returns all blocks located above the target block to their starting postitions.
def returnBlocks(target, array):
    #row, col = []
    row, col = findBlock(target, array)
    limit = len(array) - (len(array) - row - 1)

    for i in range(limit,len(array)):
        value = array[col][i]
        if value == None:
            continue
        array[col][i] = None
        array[value][0] = value
    return 

#moveOnto: src = source block, dst = destination block, array = the working array
#A function that moves the src block on top of the dst block.
def moveOnto(src, dst, array):
    returnBlocks(src,array)
    returnBlocks(dst, array)
    dstRow,dstCol = findBlock(dst,array)
    srcRow,srcCol = findBlock(src,array)
    value = array[srcCol][srcRow]
    array[dstCol][dstRow + 1] = value
    array[srcCol][srcRow] = None
    return

#moveOver: src = source block, dst = destination block, array = the working array
#A function that moves the src block on top of the stack containing the dst block.
def moveOver(src, dst, array):
    returnBlocks(src,array)
    dstRow, dstCol = findBlock(dst,array)
    srcRow, srcCol = findBlock(src,array)
    value = array[srcCol][srcRow]

    for i in range(len(array)):
        if array[dstCol][i] == None:
            array[dstCol][i] = value
            array[srcCol][srcRow] = None
            break
    return

#pileOnto: src = source block, dst = destination block, array = the working array
#A function that moves the src block and all blocks above it onto the dst block.
def pileOnto(src, dst, array):
    returnBlocks(dst, array)
    dstRow, dstCol = findBlock(dst, array)
    srcRow, srcCol = findBlock(src, array)

    for i in range(srcRow,len(array)):
        if array[srcCol][i] == None:
            break
        value = array[srcCol][i]
        
        for j in range(len(array)):
            if array[dstCol][j] == None:
                array[dstCol][j] = value
                array[srcCol][i] = None
                break
    return

#pileOver: src = source block, dst = destination block, array = the working array
#A function that moves the src block and all blocks above it onto the stack containing the dst block.
def pileOver(src, dst, array):
    dstRow, dstCol = findBlock(dst, array)
    srcRow, srcCol = findBlock(src, array)

    for i in range(srcRow,len(array)):
        if array[srcCol][i] == None:
            break
        value = array[srcCol][i]
        
        for j in range(len(array)):
            if array[dstCol][j] == None:
                array[dstCol][j] = value
                array[srcCol][i] = None
                break
    return

#writeOut: array = the working array
#A Function that write out all integer values and formats them for the output file. Also close all file objects.
def writeOut(array):
    for i in range(len(array)):
        if i == 0:
            outputFile.write(str(i) + ":")
        else:
            outputFile.write("\n" + str(i) + ":")
        for j in range(len(array)):
            if array[i][j] != None:
                outputFile.write(" " + str(array[i][j]))
            
    return

#Usage check to ensure the correct number of args
if (len(sys.argv) != 3): 
	print ('Usage: python <InputFile.txt> <OutputFile.txt>\n')
	quit()

#Get file names from the command line
inFile = sys.argv[1]
outFile = sys.argv[2]

#Opening File objects
inputFile = open(inFile, "r")
outputFile = open(outFile, "w+")

#Read line from inout file and strip white space/ new line characters
cmdline = (inputFile.readline()).rstrip()

#Set total number on blocks in problem and cast type to integer.
numOfBlocks = int(cmdline)

#Initialize the array with requireed number of blocks
array = initBlockList(numOfBlocks)

#While loop used to iterate through the command list until termination statment is reached
while True:
    #Read next line from input file
    cmdline = (inputFile.readline()).rstrip()
    
    phrase = cmdline.split()

    #Check to ensure a alid command exists and assign values
    if len(phrase) == 4:
        action = phrase[0]
        subaction = phrase[2]
        source = int(phrase[1])
        dest = int(phrase[3])
        
    #Check that action = quit. Then write output and exit
    else:
        action = phrase
        if action[0] == "quit":
            writeOut(array)
            outputFile.close()
            inputFile.close()
            sys.exit()
    
    #Check action and subaction are valid commands
    if action != "move" and action != "pile":
        print ("invalid command found in file")

    #If command contains move and over, execute with values
    elif action == "move" and subaction == "over":
        moveOver(source, dest, array)
       
    #If command contains move and onto, execute with values 
    elif action == "move" and subaction == "onto":
        moveOnto(source, dest, array)

    #If command contains pile and over, execute with values
    elif action == "pile" and subaction == "over":
        pileOver(source, dest, array)

    #If command contains pile and onto, execute with values
    elif action == "pile" and subaction == "onto":
        pileOnto(source, dest, array)  

        