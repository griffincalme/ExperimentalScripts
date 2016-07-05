import random


def CoinFlip():
    randNumber = random.randint(0,1)
    if (randNumber == 0):
        return 'heads'
    elif (randNumber == 1):
        return 'tails'
    else:
        return 'error'


for i in range(0, 10):
    print(CoinFlip())
