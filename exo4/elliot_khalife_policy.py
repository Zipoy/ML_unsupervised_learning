from agent import Agent
import numpy as np


def elliot_khalife_policy(agent: Agent) -> str:
    """
        Policy of the agent
        return "left", "right", or "none"
    """

    actions = ["left", "right", "none"]
    
    if agent.position == 0:
        action = "right"
    elif agent.position == len(agent.known_rewards) - 1:
        action = "left"
    else:
        left_reward = agent.known_rewards[agent.position - 1]
        right_reward = agent.known_rewards[agent.position + 1]
        if left_reward > right_reward:
            action = "left"
        elif right_reward > left_reward:
            action = "right"
        else:
            action = np.random.choice(["left", "right"])
    
    assert action in actions
    return action
