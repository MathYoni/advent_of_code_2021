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

    if i[0][0] == i[1][0]:

        large = max(i[0][1], i[1][1])
        small = min(i[0][1], i[1][1])

        for j in range(small, large + 1):

            if (i[0][0], j) not in vents:

                vents[(i[0][0], j)] = 1

            else:

                vents[(i[0][0], j)] += 1

    elif i[0][1] == i[1][1]:

        large = max(i[0][0], i[1][0])
        small = min(i[0][0], i[1][0])

        for j in range(small, large + 1):

            if (j, i[0][1]) not in vents:

                vents[(j, i[0][1])] = 1

            else:

                vents[(j, i[0][1])] += 1  

    else:

        # continue (Part 1)

        xchange = i[1][0] - i[0][0]
        ychange = i[1][1] - i[0][1]

        smallx = min(i[0][0], i[1][0])
        largex = max(i[0][0], i[1][0])
        smally = min(i[0][1], i[1][1])
        largey = max(i[0][1], i[1][1])


        if ychange / xchange == 1:

            for j in range(abs(xchange) + 1):

                if (smallx + j, smally + j) not in vents:

                    vents[(smallx + j, smally + j)] = 1

                else:

                    vents[(smallx + j, smally + j)] += 1   

        else:   
                        
            for j in range(abs(xchange) + 1):

                if (smallx + j, largey - j) not in vents:

                    vents[(smallx + j, largey - j)] = 1

                else:

                    vents[(smallx + j, largey - j)] += 1 



hotspots = 0

for i in vents:

    if vents[i] > 1:

        hotspots += 1

print(hotspots)
