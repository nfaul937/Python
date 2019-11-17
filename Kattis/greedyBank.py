import heapq

lineCount, timeLimit = input().split()
timeLimit = int(timeLimit)
lineCount = int(lineCount)

line = []
priorityline = []

sum = 0
for i in range(lineCount):
    deposit, maxWait = input().split()
    line.append((int(maxWait), int(deposit)))

line.sort(reverse=True)
print(line)

j = 0 
for i in range(timeLimit + 1):
    while j < lineCount and line[j][0] >= timeLimit:
        heapq.heappush(priorityline, -line[j][1])
        j+=1
    if priorityline:
        sum -= heapq.heappop(priorityline)
    timeLimit -= 1

print(sum)    