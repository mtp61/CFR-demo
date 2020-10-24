import numpy as np
from random import random


ROCK = 0
PAPER = 1
SCISSORS = 2
NUM_ACTIONS = 3


def main():
    s1, s2 = train(100)
    
    s1 = getAverageStrategy(s1)
    s2 = getAverageStrategy(s2)

    print(s1, s2)


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
    

def train(iterations):
    # ROCK, PAPER, SCISSORS
    regretSum = np.zeros(NUM_ACTIONS)
    #strategy = np.zeros(NUM_ACTIONS)
    strategySum = np.zeros(NUM_ACTIONS)
    actionUtility = np.zeros(NUM_ACTIONS)

    oppRegretSum = np.zeros(NUM_ACTIONS)
    #oppStrategy = np.zeros(NUM_ACTIONS)
    oppStrategySum = np.zeros(NUM_ACTIONS)
    oppActionUtility = np.zeros(NUM_ACTIONS)

    for i in range(iterations):
        strategy = getStrategy(regretSum)
        oppStrategy = getStrategy(oppRegretSum)
        strategySum += strategy
        oppStrategySum += oppStrategy

        action = getAction(strategy)
        oppAction = getAction(oppStrategy)
        
        actionUtility[otherAction] = 0
        actionUtility[(otherAction + 1) % NUM_ACTIONS] = 1
        actionUtility[(otherAction - 1) % NUM_ACTIONS] = -1
        oppActionUtility[action] = 0
        oppActionUtility[(action + 1) % NUM_ACTIONS] = 1
        oppActionUtility[(action - 1) % NUM_ACTIONS] = -1

        regretSum += actionUtility - actionUtility[action]
        oppRegretSum += oppActionUtility - oppActionUtility[oppAction]

    return strategySum, oppStrategySum


def getAverageStrategy(strategySum):
    return strategySum / np.sum(strategySum)
    

if __name__ == '__main__':
    main()
