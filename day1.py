f = open("day1.txt")
r = f.read().split()
s = []
for i in r:
    s.append(int(i))

### PART 1 ###

def dives(depths):
    dives = 0
    for i in range(len(depths)-1):
        if depths[i+1] - depths[i] > 0:
            dives += 1

    return dives

print(dives(s))

### PART 2 ###

tridepths = []
for i in range(len(s)-2):
    tridepths.append(s[i] + s[i+1] + s[i+2])

print(dives(tridepths))

