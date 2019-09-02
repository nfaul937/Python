import sys

inputFile = open("blocksTestIn.txt", "r")

#Read line from inout file and strip white space/ new line characters
cmdline = (inputFile.readline()).rstrip()

#Set total number on blocks in problem and cast type to integer.
blocks = int(cmdline)
print(type(blocks)) ###################################   TEMP
print(blocks) #########################################   TEMP


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
    
    
        
        