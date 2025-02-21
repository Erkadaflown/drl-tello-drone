from magent2.environments import battle_v4
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

class MagentBattleWrapper(gym.Env):
    def __init__(self, map_size=12, render_mode="rgb_array", max_steps=100):
        super().__init__()

        self.env = battle_v4.env(map_size=map_size, render_mode=render_mode)
        self.agents = self.env.possible_agents
        self.current_agent_index = 0
        self.max_steps = max_steps
        self.current_step = 0

        self.action_space = self.env.action_space(self.agents[0])
        self.observation_space = self.env.observation_space(self.agents[0])

        self.reset()
    
    def reset(self, seed=None, options=None):
        self.env.reset(seed=seed, options=options)
        self.current_agent_index = 0
        self.current_step = 0
        return self.env.observe(self.agents[self.current_agent_index])

    def step(self, action):
        """ Takes a step in the environment for the current agent. """
        agent = self.agents[self.current_agent_index]
        self.env.step(action)

        self.current_agent_index = (self.current_agent_index + 1) % len(self.agents)
        self.current_step += 1

        observation = self.env.observe(self.agents[self.current_agent_index])
        reward = self.env.rewards[agent]
        done = self.env.terminations[agent] or self.env.truncations[agent]
        info = {}

        return observation, reward, done, info

    def render(self):
        return self.env.render()

    def close(self):
        self.env.close()

env = MagentBattleWrapper(map_size=12, render_mode="rgb_array")

plt.ion()
fig, ax = plt.subplots()

obs = env.reset()

for _ in range(100):
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)

    img = env.render()
    ax.clear()
    ax.imshow(img)
    plt.pause(0.05)

    if done:
        obs = env.reset()

plt.ioff()
plt.show()
env.close()