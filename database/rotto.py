import random

dice = []
for i in range(0,10):
    n = random.randint(1,6)
    dice.append(n)

#print(dice)

lotto = []
while len(lotto) < 6:
    n = random.randint(1,45)
    if n not in lotto:
        lotto.append(n)

print(lotto)