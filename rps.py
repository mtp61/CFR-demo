import numpy as np
import matplotlib.pyplot as plt


ROCK = 0
PAPER = 1
SCISSORS = 2

ACTIONS = np.array([0, 1, 2])

def main():
    n_iter = 10000
    
    # make vectors to store the strategies and regrets
    cum_regrets = np.zeros(3)
    strat_sum = np.zeros(3)

    opp_strat = np.array([.1, .6, .3])
    
    vals = []

    # main loop
    for i in range(n_iter):
        strat = getStrategy(cum_regrets)
        strat_sum += strat

        action = np.random.choice(ACTIONS, p=strat)
        opp_action = np.random.choice(ACTIONS, p=opp_strat)

        payoff = getPayoff(action, opp_action)
        cum_regrets += getRegrets(payoff, opp_action)

        vals.append(getValue(strat_sum / (i+1), opp_strat))

    # output
    print(strat_sum / n_iter)

    # plot
    plt.plot(list(range(n_iter)), vals)
    plt.show()


def getValue(strat, opp_strat):
    val = 0
    for a1 in ACTIONS:
        for a2 in ACTIONS:
           val += strat[a1] * opp_strat[a2] * getPayoff(a1, a2)
    return val


def getStrategy(r):
    rel = r - np.mean(r)  # I added this, not sure what the impact really is but it seemed
                          # that the strategy should be computed using the mean adjusted regret
    pos_regret = np.sum(np.maximum(rel, 0))
    if pos_regret > 0:
        return np.clip(rel, 0, None) / pos_regret
    return np.ones(3) / 3


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


def getRegrets(payoff, opp_action):
    return np.array([getPayoff(a, opp_action) - payoff for a in ACTIONS])

if __name__ == '__main__':
    main()
