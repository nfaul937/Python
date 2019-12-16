'''
File: ClosestVillage.py
Program author(s): Nick Faul
ClassName: Analysis of Algorithims
Assignment: Connecting Bhutanese Villages
Due date: 11/05/2019

Brief description: 
The program takes in inout from the user. The first line is the number of cities. Following that a line is accepted for each city and place into a list. 
The program then sorts the cites based on the x and y coordinates. Once the lists are sorted a call is made to the closest pair method.
'''
import math
import sys
import time

def dist(p1, p2):
    #Returns the distance between point 1 and point 2
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def bruteForce(xSorted):
    #Find distance between points
    minDist = dist(xSorted[0], xSorted[1])
    p1 = xSorted[0]
    p2 = xSorted[1]
    xSortedLength = len(xSorted)

    #If there are only two point in the list, return the distance between them with points
    if xSortedLength == 2:
        return p1, p2, minDist

    #Otherwise, check distnace against every other point in xSorted.
    for i in range(xSortedLength-1):
        for j in range(i + 1, xSortedLength):
            if i != 0 and j != 1:
                newDistNum = dist(xSorted[i], xSorted[j])
                
                #If the new distance is less than the previous keep it instead and take the points
                if newDistNum < minDist:  
                    minDist = newDistNum
                    p1, p2 = xSorted[i], xSorted[j]

    return p1, p2, minDist

def closestPair(xSorted, ySorted):
    xSortedLength = len(xSorted)  

    #If the length is <= 3 then just work it out with brute force
    if xSortedLength <= 3:
        return bruteForce(xSorted)  
        
    #Finding the middle of xSorted
    mid = xSortedLength // 2  
    
    #Splitting the xSorted array into two halves
    LxSorted = xSorted[:mid]  
    RxSorted = xSorted[mid:]
    
    #Assigning the actual midpoint
    midpoint = xSorted[mid][0]

    #Split ySorted in two halves using the midpoint
    LySorted = []
    RySorted = []
    for x in ySorted:  
        if x[0] <= midpoint:
           LySorted.append(x)
        else:
           RySorted.append(x)
    
    #Call closestPairs on both left arrays and both right arrays
    p1, p2, dist1 = closestPair(LxSorted, LySorted)
    p3, p4, dist2 = closestPair(RxSorted, RySorted)
    
    #Check and see which return is has less distance and take it
    if dist1 <= dist2:
        distance = dist1
        pts = p1, p2
    else:
        distance = dist2
        pts = p3, p4
    
    #Check to see if there are any cities the cross the middle line with less distance
    p5, p6, dist3 = closestMidPair(xSorted, ySorted, distance, pts)
    
    #If the distance over the middle is less that current value take it instead
    if distance <= dist3:
        return pts[0], pts[1], distance

    else:
        return p5, p6, dist3

def closestMidPair(xArray, yArray, d, bestSet):
    #Find length of xArray
    xLength = len(xArray) 
    #Find and assign midpoint for xArray 
    mid = xArray[xLength // 2][0]  
    
    dxArray = []
    #Grab points that are withing the best distance from the midpoint and place them into and array
    for point in yArray:
        if mid - d <= point[0] <= mid + d:
            dxArray.append(point)

    bestDist = d  
    dxLength = len(dxArray)  

    #Check each point against the nest seven points.
    #Take the best distance
    for i in range(dxLength - 1):
        for j in range(i+1, min(i + 7, dxLength)):
            p, q = dxArray[i], dxArray[j]
            dst = dist(p, q)
            if dst < bestDist:
                bestSet = p, q
                bestDist = dst
    return bestSet[0], bestSet[1], bestDist


#Take in number of cities
numOfCity = int(input())

#Init lists
cities = []
xSorted = []
ySorted = []

#Take in each line as a tuple and store it
for i in range(0,numOfCity):
    line = input().split()
    if len(line) == 4:
        line[2] = line[2] + ' ' + line[3]
    tup = (float(line[0]), float(line[1]), line[2])
    cities.append(tup)

start = time.time()
#Sort each list one the x and y coords respectivly
xSorted = sorted(cities, key=lambda x: x[0])
ySorted = sorted(cities, key=lambda x: x[1])

#Call to find closest pair

p1, p2, minDist = closestPair(xSorted, ySorted)
end = time.time()

print()
print(end - start)
print('{:.2f} between {} and {}'.format(minDist, str(p1[2]), str(p2[2])))
#print("%.2f between" % (minDist, str(p1[2]), str(p2[2])))

