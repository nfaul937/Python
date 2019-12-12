import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

numOfCity = int(input())

cities = []

for i in range(0,numOfCity):
    cities.append(input().split())

for i in range(int(numOfCity)):
    print(cities[i][2])
