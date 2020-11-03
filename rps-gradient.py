import numpy as np
import matplotlib.pyplot as plt


ROCK = 0
PAPER = 1
SCISSORS = 2

ACTIONS = np.array([0, 1, 2])

def main():
    n_iter = 100
    alpha = .001

    # make vectors to store the strategies
    strat = np.ones(3) / 3

    opp_strat = np.array([.1, .6, .3])
    
    vals = []

    # main loop
    for i in range(n_iter):
        strat += alpha * getDerivatives(opp_strat)
        strat = normalize(strat)

        vals.append(getValue(strat, opp_strat))

    # output
    print(strat)

    # plot
    plt.plot(list(range(n_iter)), vals)
    plt.show()


def getValue(strat, opp_strat):
    val = 0
    for a1 in ACTIONS:
        for a2 in ACTIONS:
           val += strat[a1] * opp_strat[a2] * getPayoff(a1, a2)
    return val


def getPayoff(action, opp_action):
    if action == opp_action:
        return 0
    if action == ROCK:
        if opp_action == SCISSORS:
            return 1
        return -1
    elif action == SCISSORS:
        if opp_action == PAPER:
            return 1
        return -1
    else:  # PAPER
        if opp_action == ROCK:
            return 1
        return -1


def getDerivatives(s):
    d = np.zeros(3)
    for i in range(3):
        for j in range(3):
            d[i] += s[j] * getPayoff(i, j)
    return d


def normalize(s):
    rel = s - np.mean(s)
    p = np.sum(np.maximum(rel, 0))
    if p > 0:
        return np.clip(rel, 0, None) / p
    return np.ones(3) / 3


if __name__ == '__main__':
    main()
