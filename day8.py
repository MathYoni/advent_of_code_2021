import re
f = open("day8.txt")
r = f.read().splitlines()
s = []

for i in r:

    m = re.search(r'(\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S) (\S+) (\S+) (\S+) (\S+)', i)
    lin = []
    lout = []

    for j in range(10):

        lin.append(set(m.group(j+1)))

    for j in range(4):

        lout.append(set(m.group(j+12)))

    t = [lin, lout]

    s.append(t)

#### PART 1 ####

# digits = 0

# for i in s:
    
#     for j in i[1]:

#         l = len(j)

#         if l == 2 or l == 3 or l == 4 or l == 7:

#             digits += 1

# print(digits)

#### PART 2 ####

def decoder(digs):

    digs[0].sort(key=len)
    counter = -1
    code = []

    while counter < 9:

        a = digs[0][counter]

        if counter == -1:

            code.append((8,a))

        elif counter == 0:

            code.append((1,a))

        elif counter == 1:

            code.append((7,a))

        elif counter == 2:

            code.append((4,a))

        else:

            l = len(a)

            if l == 6:

                if a.intersection(code[3][1]) == code[3][1]:

                    code.append((9,a))

                elif len(a.intersection(code[1][1])) == 1:

                    code.append((6,a))

                else:

                    code.append((0,a))

            else:

                if a.union(code[3][1]) == code[0][1]:

                    code.append((2,a))

                elif a.intersection(code[1][1]) == code[1][1]:

                    code.append((3,a))

                else:

                    code.append((5,a))

        counter += 1

    return code

total = 0

for i in s:

    sum = 0
    codes = decoder(i)
    counter = 0
    
    while counter < 4:

        for j in codes:

            if i[1][counter] == j[1]:

                sum += j[0] * (10**(3-counter))

        counter += 1

    total += sum

print(total)
            





        

        






