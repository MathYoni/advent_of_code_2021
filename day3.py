f = open("day3.txt")
r = f.read().splitlines()

##### Not proud of my code on this one... got very sleepy #####

def colcount(diag, col):
        
    zeroes = 0
    ones = 0

    for j in diag:
        if j[col] == "0":
            zeroes += 1
        else:
            ones += 1

    if zeroes > ones:
        return 0

    else:
        return 1

def bintoint(k):

    k.reverse()
    integer = 0
    exponent = 0

    for i in range(len(k)):
        integer += k[i] * (2**exponent)
        exponent += 1

    return integer

##### PART 1 #####

# gamma = []
# epsilon = []

# for i in range(len(r[0])):    

#     if colcount(r, i):
#         gamma.append(0)
#         epsilon.append(1)

#     else:
#         gamma.append(1)
#         epsilon.append(0)

# print(bintoint(gamma) * bintoint(epsilon))

##### PART 2 #####

def subdiv(diag, digit, col):
    
    newlist = []

    for i in diag:
        if i[col] == digit:
            newlist.append(i)

    return newlist

oxy = r
carb = r

for i in range(len(r[0])):

    if len(oxy) == 1:
        pass

    elif colcount(oxy, i) == 1:
        
        oxy = subdiv(oxy, "1", i)

    elif colcount(oxy, i) == 0:

        oxy = subdiv(oxy, "0", i)

    if len(carb) == 1:
        pass

    elif colcount(carb, i) == 1:
       
        carb = subdiv(carb, "0", i)

    elif colcount(carb, i) == 0:
        
        carb = subdiv(carb, "1", i)

oxybin = []
carbbin = []

for i in range(len(oxy[0])):
    
    oxybin.append(int(oxy[0][i]))
    carbbin.append(int(carb[0][i]))

print(bintoint(oxybin) * bintoint(carbbin))





