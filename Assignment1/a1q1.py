import random


random.choice([1,2,3,4,5,6])

a_wins=0
b_wins=0
draws=0

for jj in range(1000):
    counta=0
    countb=0
    for i in range(10):
        a = (random.choice([1,2,3,4,5,6])==2) | (random.choice([1,2,3,4,5,6])==3) | (random.choice([1,2,3,4,5,6])==5)
        b = (random.choice([1,2,3,4,5,6])==2) | (random.choice([1,2,3,4,5,6])==3) | (random.choice([1,2,3,4,5,6])==5)
        counta+=int(a)
        countb+=int(b)

    a = (random.choice([1,2,3,4,5,6])==2) | (random.choice([1,2,3,4,5,6])==3) | (random.choice([1,2,3,4,5,6])==5)
    counta += a

    if (counta>countb):
        a_wins+=1
    elif (counta<countb):
        b_wins+=1
    else:
        draws+=1

print((a_wins/1000,b_wins/1000,draws/1000))

