import numpy as np

def optimistic_greedy_bandit(
    true_rewards: list,
    initial_q: float,
    n_steps: int,
    step_size: float
) -> tuple:
    """
    Simulate a greedy bandit agent with optimistic initialization.
    
    Args:
        true_rewards: List of true deterministic rewards for each arm
        initial_q: Optimistic initial Q-value for all arms
        n_steps: Number of steps to simulate
        step_size: Constant step-size (alpha) for Q-value updates
    
    Returns:
        Tuple of (Q_values, action_counts) where Q_values is a list of
        floats rounded to 4 decimal places, and action_counts is a list of ints.
    """
    k = len(true_rewards)
    q_values = [initial_q] * k
    counts = [0] * k
    for _ in range(n_steps):
        i = np.argmax(q_values)
        q_values[i] += step_size * (true_rewards[i]-q_values[i])
        counts[i] += 1
    
    return (q_values,counts)