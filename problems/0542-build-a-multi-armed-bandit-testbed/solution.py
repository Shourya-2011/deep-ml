import numpy as np

def create_bandit_testbed(k: int, num_pulls: int, seed: int = 42) -> tuple:
    np.random.seed(seed)
    arms = np.random.randn(k)
    
    sample_means = []
    for arm in arms:
        sample_means.append(np.mean(np.random.randn(num_pulls)+arm))

    return (np.round(arms, 4).tolist(), np.round(sample_means,4).tolist(), np.argmax(arms))
