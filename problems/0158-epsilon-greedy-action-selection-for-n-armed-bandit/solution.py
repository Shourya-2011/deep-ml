import numpy as np

def epsilon_greedy(Q, epsilon=0.1):
    u = np.random.rand()
    if u < epsilon:
        return float(np.random.choice(len(Q)))
    else:
        return float(np.argmax(Q))