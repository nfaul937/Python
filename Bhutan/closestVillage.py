
numOfCity = int(input())

cities = []

for i in range(0,numOfCity):
    cities.append(input().split())

for i in range(int(numOfCity)):
    print(cities[i][2])
