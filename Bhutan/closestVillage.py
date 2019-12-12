import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def bruteForce(xSorted):
    mi = dist(xSorted[0], xSorted[1])
    p1 = xSorted[0]
    p2 = xSorted[1]

    ln_xSorted = len(xSorted)

    if ln_xSorted == 2:
        return p1, p2, mi

    for i in range(ln_xSorted-1):
        for j in range(i + 1, ln_xSorted):
            if i != 0 and j != 1:
                d = dist(xSorted[i], xSorted[j])

                if d < mi:  
                    mi = d
                    p1, p2 = xSorted[i], xSorted[j]

    return p1, p2, mi

def closest_pair(xSorted, ySorted):
    ln_xSorted = len(xSorted)  

    if ln_xSorted <= 3:
        return bruteForce(xSorted)  

    mid = ln_xSorted // 2  
    Qx = xSorted[:mid]  
    Rx = xSorted[mid:]
    
    midpoint = xSorted[mid][0]  
    Qy = list()
    Ry = list()

    for x in ySorted:  
        if x[0] <= midpoint:
           Qy.append(x)
        else:
           Ry.append(x)
    
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)
    
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)
    
    (p3, q3, mi3) = closest_split_pair(xSorted, ySorted, d, mn)
    
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3

def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)  
    mx_x = p_x[ln_x // 2][0]  
    
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta  
    ln_y = len(s_y)  
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

numOfCity = int(input())

cities = []
xSorted = []
ySorted = []

for i in range(0,numOfCity):
    line = input().split()
    tup = (float(line[0]), float(line[1]), line[2])
    cities.append(tup)

xSorted = sorted(cities, key=lambda x: x[0])
ySorted = sorted(cities, key=lambda x: x[1])

p1, p2, dist = closest_pair(xSorted, ySorted)  # Recursive D&C function

print(dist)
print(p1)
print(p2)