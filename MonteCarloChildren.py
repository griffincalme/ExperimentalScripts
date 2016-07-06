#Program runs a Monte Carlo simulation to determine the probability that at least one child will be a girl

import random
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

plt.style.use('ggplot')

def CoinFlip():
    randNumber = random.randint(0,1)
    if (randNumber == 0):
        return 'boy'
        #return 'heads'
    elif (randNumber == 1):
        return 'girl'
        #return 'tails'
    else:
        return 'error'


#if I have 3 kids, what are the odds that at least one will be male
def MonteCarloKids(numTrials=100, numKids=3):

    trialsDict = dict() #dictionary of all trials
    numberWithGirl = 0 #initialize
    probabilityList = []
    powerTens = []
    decrementer = numTrials

    #iterate over number of trials in monte carlo simulation
    for i in range(0, numTrials):

        children = []
        #generate set of kids for one generation
        for j in range(0, numKids):
            children.append(CoinFlip())

        #print(children)

        trialsDict[i] = children #append set of kids to the newest generation in the dictionary

    #count the number of generations that have at least one girl
    for key in trialsDict.keys():
        if trialsDict[key].count('girl'):
            numberWithGirl = numberWithGirl + 1

        probability = (numberWithGirl / (key + 1))
        probabilityList.append(probability)


    #for key in trialsDict.keys():
        #if (key + 1) % 10 == 0:
             #print('Probability at trial ' + str(key + 1) + ' is ' + str(probabilityList[key]))


    #generate log scale for trials
    while decrementer >= 1:
        powerTens.append(decrementer)
        decrementer = decrementer / 10

    powerTens.reverse()

    for k in powerTens:
        k = int(k)
        print('Trial: ' + str(k) + ', estimated probability: ' + str(probabilityList[k - 1]))


    print('------')
    print('Odds of having at least one boy are: ' + str(numberWithGirl / numTrials))



    plt.semilogx(list(range(numTrials)), probabilityList)
    plt.title('Probility of having at least 1 girl')
    plt.grid(True)
    plt.ylabel('estimated probability')
    plt.xlabel('simulation number')
    plt.ylim(ymin=0, ymax=1.5)
    plt.show()


#(number of trials, number of kids planned for one generation)
MonteCarloKids(1000000, 3)
