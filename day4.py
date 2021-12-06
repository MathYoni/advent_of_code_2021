f = open("day4.txt")
r = f.read().splitlines()

s = r[0].split(',')
callouts = [int(i) for i in s]

r.remove(r[0])
r.remove(r[1])

bingocards = []
bingochecks = []

counter = 0
cardcounter = 0
newcard = {}

while counter < len(r):
        
    if r[counter] != '':
    
        t = r[counter].split()
            
        for i in t:

            a = int(i)
            card[a] = [cardcounter//5 + 1, cardcounter%5 + 1 , 0]
            cardcounter += 1
            
        counter += 1

    else:
        
        card = newcard
        newcard = {}
        bingocards.append(card)
        bingochecks.append([0,0,0,0,0,0,0,0,0,0,0])
        counter += 1
        cardcounter = 0

winner = False
last = False
complete = 0

for i in callouts:
    
    j = 0

    while j < len(bingocards):
        
        if i in bingocards[j]:
            
            a = bingocards[j][i][0]
            b = bingocards[j][i][1]
            bingocards[j][i][2] = 1
            bingochecks[j][a-1] += 1
            bingochecks[j][b+4] += 1
            
            if max(bingochecks[j]) == 5 and bingochecks[j][-1] == 0:

                bingochecks[j][-1] = 1
                complete += 1
                
                if complete == len(bingocards):
                    
                    print(j, "is winner")
                    windex = j
                    winnum = i
                    winner = True
                    break

                # else:

                #     bingochecks.remove(bingochecks[j])
                #     bingocards.remove(bingocards[j])
        
        j += 1
    
    if winner:
        
        break

    # if complete == len(bingocards) == 1:
        
    #     last = True

wincard = bingocards[windex]
wincheck = bingochecks[windex]

uncalled = 0

for i in wincard:
    if wincard[i][2] == 0:
        uncalled += i

print(uncalled * winnum)





