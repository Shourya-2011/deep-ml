import numpy as np

def ucb_action(counts, values, t, c):
    """
    Choose an action using the UCB1 formula.
    Args:
      counts (np.ndarray): Number of times each action has been chosen
      values (np.ndarray): Average reward of each action
      t (int): Current timestep (starts from 1)
      c (float): Exploration coefficient
    Returns:
      int: Index of action to select
    """
    k = len(counts)
    highest_ucb = 0
    index = 0

    for i in range(k):
      cur = values[i]+ (c * np.sqrt(np.log(t)/counts[i]))
      if cur > highest_ucb:
        highest_ucb = cur
        index = i

    return index 