'''
File: greedyBank_Faul.py
Program author(s): Nick Faul
ClassName: Analysis of Algorithims
Assignment: Dynamic or Greedy Lab
Due date: 11/15/2019

Brief description: 
This program first reads from standard input a number of customers in line and the number of minutes until close.
The progam then reads in a deposit and max wait time for each customer. 
The program then sorts the people in a list and selects them based on the max deposit from each wait time group.
The maximum deposit from each group is the added together for the sum.
'''
import heapq

#read in number of people and time until close
lineCount, timeLimit = input().split()

#Variable initiation
timeLimit = int(timeLimit)
lineCount = int(lineCount)
line = []
priorityline = []
sum = 0

#Read in input for each person in the format deposit, wait time.
#Add each person to a list
for i in range(lineCount):
    deposit, maxWait = input().split()
    line.append((int(maxWait), int(deposit)))

#Sort the list in descending order for both wait and deposit
line.sort(reverse=True)

j = 0 
#Starting from the longest wait, push each person on the heap
for i in range(timeLimit + 1):
    #While people are still in line push people to the heap
    while j < lineCount and line[j][0] >= timeLimit:
        heapq.heappush(priorityline, -line[j][1])
        j+=1
    #If heap has values, pop the largest(least) and figure sum
    if priorityline:
        sum -= heapq.heappop(priorityline)
    timeLimit -= 1

print(sum)    