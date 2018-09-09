import random

land=('g','c','w')
other_side = []

def check(chck):
    g = 'g'
    c = 'c'
    w = 'w'
    if g and c in chck():
        return 0
    elif g and w in chck():
        return 0
    else:
        return 1
land = list(land)

while len(other_side) != 4:
    boat = []
    boat = random.choices(land,2)
    land.remove(boat[0],boat[1])
    if ~check(land):
        continue
    else:
        if check(boat):
            other_side = boat
            boat.clear()
        else:
            other_side = random.choice(boat)
            land.append(NULL)
else:
    print("faliure")


        
    

