import re
f = open("day5.txt")
r = f.read().splitlines()
s = []

for i in r:

    m = re.search(r'(\d+),(\d+) -> (\d+),(\d+)', i)
    l = [[int(m.group(1)), int(m.group(2))], [int(m.group(3)), int(m.group(4))]]
    s.append(l)

vents = {}

for i in s:
    
    delta = abs(i[1][0] - i[0][0]) + abs(i[1][1] - i[0][1]) 
    dx = (i[1][0] - i[0][0]) / delta
    dy = (i[1][1] - i[0][1]) / delta

    if dx != 0 and dy != 0:

        #continue #(Part 1)
        dx = 2*dx
        dy = 2*dy
        delta = int(delta/2)

    for j in range(delta + 1):

        a = j*dx
        b = j*dy

        if (i[0][0] + a, i[0][1] + b) not in vents:

            vents[(i[0][0] + a, i[0][1] + b)] = 1

        else:

            vents[(i[0][0] + a, i[0][1] + b)] += 1



hotspots = 0

for i in vents:

    if vents[i] > 1:

        hotspots += 1

print(hotspots)
