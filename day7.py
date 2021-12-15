import math
f = open("day7.txt")
r = f.read().split(",")
s = []

for i in r:

    s.append(int(i))

fuels = []

for i in range(min(s), max(s)+1):

    sum = 0

    for j in s:
        
        n = (abs(j-i)+1)

        #sum += n #Part 1
        sum += int((n*(n-1))/2) #Part 2

    fuels.append(sum)

print(min(fuels))






