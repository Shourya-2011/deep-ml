def exp_weighted_average(Q1, rewards, alpha):
    """
    Q1: float, initial estimate
    rewards: list or array of rewards, R_1 to R_k
    alpha: float, step size (0 < alpha <= 1)
    Returns: float, exponentially weighted average after k rewards
    """
    k = len(rewards)

    # Term 1
    T1 = (1-alpha)**k
    T1 *= Q1

    # Term 2
    T2 = 0
    for i in range(1,k+1):
        T2 += (alpha * ((1-alpha)**(k-i))) * rewards[i-1]
    
    return T1+T2