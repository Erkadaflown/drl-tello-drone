import gymnasium as gym
import numpy as np

class CustomEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.observation_space = gym.spaces.Box(low=0, high=10, shape=(2,), dtype=np.float32)  # Example state
        self.action_space = gym.spaces.Discrete(3)  # Example: 3 actions (0, 1, 2)

    def reset(self, seed=None, options=None):
        """Resets the environment at the beginning of an episode"""
        observation = np.array([5.0, 5.0], dtype=np.float32)
        return observation, {}  # Observation and empty info dict

    def step(self, action):
        """Takes an action and returns next state, reward, done flag, and info"""
        observation = np.array([np.random.rand(), np.random.rand()], dtype=np.float32)  # Random new state
        reward = np.random.rand()  # Random reward
        done = np.random.rand() > 0.9  # 10% chance of ending episode
        return observation, reward, done, False, {}

    def render(self):
        """Visualizes the environment"""
        print("Rendering environment...")  # Placeholder

    def close(self):
        """Closes the environment"""
        print("Closing environment...")

# **Testing the environment**
env = CustomEnv()
obs, _ = env.reset()

for _ in range(10):  # Run 10 steps
    action = env.action_space.sample()  # Take random action
    obs, reward, done, _, _ = env.step(action)
    print(f"Action: {action}, Observation: {obs}, Reward: {reward}, Done: {done}")
    if done:
        env.reset()

env.close()
