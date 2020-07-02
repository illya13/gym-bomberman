OpenAI Gym Bomberman Env
[https://gym.openai.com/](https://gym.openai.com/)

# Installation
Download `enriched.zip` from [Google Drive](https://drive.google.com/drive/folders/1GBYH9hBdGEIpRlbTvMJnGYgd4E9KasqX)
and extract into `gym_bomberman/envs/data` subfolder 

```bash
pip install -e .
```

# Envs
- `gym_bomberman:Bomberman-v0` - env based on random file from data` subfolder
- `gym_bomberman:Bomberman-all-v0` - env over all files from `data` subfolder
- `gym_bomberman:Bomberman-15mmite2rhbuendm8atj-v0` - env based on `15mmite2rhbuendm8atj.raw` file
There are other concrete file based ens please see [gym_bomberman/__init__.py](gym_bomberman/__init__.py)

# Usage
```python
import gym

env = gym.make('gym_bomberman:Bomberman-v0')
# OR
env = gym.make('gym_bomberman:Bomberman-all-v0')
# OR
env = gym.make('gym_bomberman:Bomberman-15mmite2rhbuendm8atj-v0')
```

# Full `replay` example
```python
import gym
import os
import time

env = gym.make('gym_bomberman:Bomberman-v0')

while True:
    obs = env.reset()
    if obs is None:
        break

    action = env.action_space.sample()
    while True:
        os.system('cls')

        env.render()

        print(obs)
        print()
        print(action)
        time.sleep(0.05)

        obs, reward, done, info = env.step(action)
        if done:
            break

        action = info["action"]

env.close()
```