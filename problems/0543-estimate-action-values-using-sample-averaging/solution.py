import numpy as np

def sample_average_action_values(k: int, actions: list, rewards: list) -> tuple:
    
    counts = np.zeros(k, dtype=int)
    acc_rewards = np.zeros(k)

    for action,reward in zip(actions,rewards):
        counts[action] +=1 
        acc_rewards[action] += reward
    
    return tuple([
    np.round(np.divide(acc_rewards,counts, where=counts>0),4).tolist(),
    counts.tolist()])