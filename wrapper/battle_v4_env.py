from magent2.environments import battle_v4
import magent2
import matplotlib.pyplot as plt

env = battle_v4.env(
    map_size=12,
    render_mode="rgb_array"
)

env.reset()

plt.ion()
fig, ax = plt.subplots()

for _ in range(100):
    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        if termination or truncation:
            action = None
        else:
            action = env.action_space(agent).sample()
        
        env.step(action)
        img = env.render()
        ax.clear()
        ax.imshow(img)
        plt.pause(0.05)

plt.ioff()
plt.show()
env.close()