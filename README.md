[OpenAI Gym](https://gym.openai.com/) Bomberman Env

More info about Bomberman and Environment
- https://en.wikipedia.org/wiki/Bomberman
- https://dojorena.io/games/1
- https://dojorena.io/manuals/43


# Observation Space
Dictionary over:
- board: 2D Box corresponding to raw Board data
- bombs: `0..5` - currently number of bombs placed by a player
- perks: `0..100`, `0..100`, `0..100` - active time by perks: `bomb_blast_radius_increase`, `bomb_count_increase`, `bomb_immune`
```python
    observation_space = spaces.Dict({
        'board': spaces.Box(low=0, high=ord('V')-ord('A'), shape=(SIZE, SIZE), dtype=np.uint8),
        'bombs': spaces.Discrete(6),
        'perks': spaces.MultiDiscrete([100, 100, 100])
    })
```
Please check [gym_bomberman/envs/bomberman_env.py](gym_bomberman/envs/bomberman_env.py) for the details


# Action Space
- `ACT` before movement: 0-No, 1-Yes
- movement into some direction: 0-`""`, 1-`"UP"`, 2-`"DOWN"`, 3-`"LEFT"`, 4-`"RIGHT"` 
- `ACT` after movement: 0-No, 1-Yes

```python
    action_space = spaces.MultiDiscrete([2, 5, 2]) 
```
Please check [gym_bomberman/envs/bomberman_env.py](gym_bomberman/envs/bomberman_env.py) for the details


# Envs
- `gym_bomberman:Bomberman-v0` - env based on random file from `data` subfolder
- `gym_bomberman:Bomberman-all-v0` - env over all files from `data` subfolder
- `gym_bomberman:Bomberman-15mmite2rhbuendm8atj-v0` - env based on `15mmite2rhbuendm8atj.raw` file. There are other concrete file based ens please see [gym_bomberman/__init__.py](gym_bomberman/__init__.py)
- `gym_bomberman:Bomberman-online-v0` - TBD


# Installation
Clone repo
```bash
git clone https://github.com/illya13/gym-bomberman.git
cd gym-bomberman
```

### Offline data
Download `enriched.zip` from [Google Drive](https://drive.google.com/drive/folders/1GBYH9hBdGEIpRlbTvMJnGYgd4E9KasqX)
and extract into `gym_bomberman/envs/data` subfolder. To get more info how the data were collected please check [https://github.com/illya13/bomberman-js](https://github.com/illya13/bomberman-js)


### Online environment integration
TBD 

### Complete installation
Run
```bash
pip install -e .
```


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
import time
import numpy as np

env = gym.make('gym_bomberman:Bomberman-v0')

while True:
    obs = env.reset()
    if obs is None:
        break

    action = np.array([0, 0, 0])
    while True:
        print()
        env.render()
        print(action)
        print()
        time.sleep(1)

        obs, reward, done, info = env.step(action)

        if done:
            break
        action = info["action"]

env.close()
```