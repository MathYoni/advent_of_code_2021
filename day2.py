f = open("day2.txt")
r = f.read().splitlines()
s = []

for i in r:
    j = i.split()
    s.append([j[0][0], int(j[1][0])])

horiz = 0
depth = 0

##### PART 1 #####

# for i in s:
#     if i[0] == 'f':
#         horiz += i[1]

#     elif i[0] == 'd':
#         depth += i[1]

#     else:
#         depth -= i[1]

##### PART 2 #####

# aim = 0

# for i in s:
#     if i[0] == 'f':
#         horiz += i[1]
#         depth += aim * i[1]

#     elif i[0] == 'd':
#         aim += i[1]

#     else:
#         aim -= i[1]

print(horiz*depth)