import numpy as np
from random import random


ROCK = 0
PAPER = 1
SCISSORS = 2
NUM_ACTIONS = 3


def main():
    print(getAverageStrategy(train(10000)))


def getStrategy(regretSum):
    strategy = np.maximum(regretSum, 0)
    normalizingSum = np.sum(strategy)
    if normalizingSum > 0:
        strategy /= normalizingSum
    else:
        strategy = np.ones(NUM_ACTIONS) / NUM_ACTIONS
    return strategy
    

def getAction(strategy):
    r = random()
    cumulativeProbability = 0
    for i, p in enumerate(strategy):
        cumulativeProbability += p
        if cumulativeProbability > r:
            return i
    

def train(interations):
    # ROCK, PAPER, SCISSORS
    regretSum = np.zeros(NUM_ACTIONS)
    strategy = np.zeros(NUM_ACTIONS)
    strategySum = np.zeros(NUM_ACTIONS)
    oppStrategy = np.array([0.4, 0.3, 0.3])
    oppStrategy = np.ones(NUM_ACTIONS) / NUM_ACTIONS

    actionUtility = np.zeros(NUM_ACTIONS)
    for i in range(interations):
        strategy = getStrategy(regretSum)
        strategySum += strategy

        myAction = getAction(strategy)
        otherAction = getAction(oppStrategy)
        
        actionUtility[otherAction] = 0
        actionUtility[(otherAction + 1) % NUM_ACTIONS] = 1
        actionUtility[(otherAction - 1) % NUM_ACTIONS] = -1

        regretSum += actionUtility - actionUtility[myAction]

    #print(regretSum, strategySum)
    return strategySum


def getAverageStrategy(strategySum):
    return strategySum / np.sum(strategySum)
    

if __name__ == '__main__':
    main()
