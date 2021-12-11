f = open("day6.txt")
r = f.read().split(',')
s = []

for i in r:
    s.append([int(i),1])

newgen = 0

generations = 257 # number of days plus one

for i in range(generations):

    if newgen != 0:
        
        s.append([8, newgen])
    
    newgen = 0
        
    count = 0

    while count < len(s):

        mod = s[count][0] % 7

        if mod == 0:

            if s[count][0] != 7: # ensures 8's don't reproduce too soon

                newgen += s[count][1]
            
        s[count][0] -= 1

        count += 1


    
total = 0

for i in s:

    total += i[1]

print(total)

