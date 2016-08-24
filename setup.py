from setuptools import setup

setup(name='gym_bomberman',
      version='0.1',
      url="https://github.com/illya13/gym_bomberman",
      license="MIT",
      packages=["gym_bomberman", "gym_bomberman.envs"],
      package_data={
            'gym_bomberman.envs': ['data/*.raw'],
      },
      install_requires=['gym']
)
