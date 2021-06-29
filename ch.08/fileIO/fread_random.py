import random

try :
    f = open('c:/pyfile/2021kbo.txt','r')
    data = f.read().split()

    n = random.randint(0,6)

    print(data[n])

    team = random.choice(data)

    print(team)

except FileNotFoundError as e:
    print(e)