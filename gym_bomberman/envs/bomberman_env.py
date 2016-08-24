import gym
from gym import error, spaces, utils
import os
import random
import json


class BombermanEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    data_files = {}
    all_index = None

    def __init__(self, filename=None, all=False):
        self._init_data_files()
        if all:
            self.all_index = 0
            filename = self._data_files_file(self.all_index)
        elif filename is None:
            filename = self._random_data_file()
        else:
            filename = self.data_files[filename]

        self.data = open(filename)
        self.observation_space = spaces.Dict({"position": spaces.Discrete(2), "velocity": spaces.Discrete(3)})

    def step(self, action):
        dict_data = self._next()
        if dict_data is None:
            return None, None, True, None

        if "action" not in dict_data:
            dict_data["action"] = []
        return dict_data, dict_data["reward"], dict_data["done"], dict_data["info"]

    def reset(self):
        while True:
            dict_data = self._next()
            if dict_data is None:
                return None
            if not dict_data["done"]:
                break
        return dict_data

    def render(self, mode='human'):
        None

    def close(self):
        self.data.close()

    def seed(self, seed=None):
        random.seed(seed)

    def _init_data_files(self):
        parent_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(parent_path, "data")

        with os.scandir(data_path) as i:
            for entry in i:
                if entry.is_file() and entry.name.endswith(".raw"):
                    self.data_files[entry.name] = os.path.join(data_path, entry.name)

    def _random_data_file(self):
        i = random.randint(0, len(self.data_files) - 1)
        keys = list(self.data_files.keys())
        return self.data_files[keys[i]]

    def _next(self):
        json_data = self.data.readline()
        try:
            return json.loads(json_data)
        except json.decoder.JSONDecodeError:
            return self._try_another_file()

    def _try_another_file(self):
        if self.all_index is not None and self.all_index + 1 < len(self.data_files):
            self.all_index += 1
            self.data.close()
            filename = self._data_files_file(self.all_index)
            self.data = open(filename)
            return self._next()
        else:
            return None

    def _data_files_file(self, index):
        keys = list(self.data_files.keys())
        key = keys[index]
        return self.data_files[key]


class BombermanEnvAll(BombermanEnv):

    def __init__(self):
        super(BombermanEnvAll, self).__init__(all=True)


class BombermanEnv_15mmite2rhbuendm8atj(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_15mmite2rhbuendm8atj, self).__init__(filename="15mmite2rhbuendm8atj.raw")


class BombermanEnv_4hhuh2kpdkkmqaa22aey(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_4hhuh2kpdkkmqaa22aey, self).__init__(filename="4hhuh2kpdkkmqaa22aey.raw")


class BombermanEnv_7na941lc1unrqembaz77(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_7na941lc1unrqembaz77, self).__init__(filename="7na941lc1unrqembaz77.raw")


class BombermanEnv_933f496rgd34y7h2kkus(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_933f496rgd34y7h2kkus, self).__init__(filename="933f496rgd34y7h2kkus.raw")


class BombermanEnv_ezhqpi31qs55fz9lgq1o(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_ezhqpi31qs55fz9lgq1o, self).__init__(filename="ezhqpi31qs55fz9lgq1o.raw")


class BombermanEnv_g0zaq08ja51gobn0nocc(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_g0zaq08ja51gobn0nocc, self).__init__(filename="g0zaq08ja51gobn0nocc.raw")


class BombermanEnv_gdqk89qftxujna71w4ur(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_gdqk89qftxujna71w4ur, self).__init__(filename="gdqk89qftxujna71w4ur.raw")


class BombermanEnv_gubljie2khm74wx8fg5w(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_gubljie2khm74wx8fg5w, self).__init__(filename="gubljie2khm74wx8fg5w.raw")


class BombermanEnv_i2t2233nlgu3jegckthq(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_i2t2233nlgu3jegckthq, self).__init__(filename="i2t2233nlgu3jegckthq.raw")


class BombermanEnv_m31eg564eubt46l48u6k(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_m31eg564eubt46l48u6k, self).__init__(filename="m31eg564eubt46l48u6k.raw")


class BombermanEnv_mhz5xg9tn0mp12tmryse(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_mhz5xg9tn0mp12tmryse, self).__init__(filename="mhz5xg9tn0mp12tmryse.raw")


class BombermanEnv_njaq471ilx8a28nvk01u(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_njaq471ilx8a28nvk01u, self).__init__(filename="njaq471ilx8a28nvk01u.raw")


class BombermanEnv_ors0qf4yh5xk95zi9l0k(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_ors0qf4yh5xk95zi9l0k, self).__init__(filename="ors0qf4yh5xk95zi9l0k.raw")


class BombermanEnv_p0p8n9fwffdxem12bje0(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_p0p8n9fwffdxem12bje0, self).__init__(filename="p0p8n9fwffdxem12bje0.raw")


class BombermanEnv_rammffc1xl9980pn9z3o(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_rammffc1xl9980pn9z3o, self).__init__(filename="rammffc1xl9980pn9z3o.raw")


class BombermanEnv_s4vmpmnhe6pr89c24hba(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_s4vmpmnhe6pr89c24hba, self).__init__(filename="s4vmpmnhe6pr89c24hba.raw")


class BombermanEnv_uzeem6y5o57fwix75qum(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_uzeem6y5o57fwix75qum, self).__init__(filename="uzeem6y5o57fwix75qum.raw")


class BombermanEnv_vy0c52iehd1sn0rlcuvf(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_vy0c52iehd1sn0rlcuvf, self).__init__(filename="vy0c52iehd1sn0rlcuvf.raw")


class BombermanEnv_wdy3hvgbcaoz2iyuwn6o(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_wdy3hvgbcaoz2iyuwn6o, self).__init__(filename="wdy3hvgbcaoz2iyuwn6o.raw")


class BombermanEnv_y2xvmwbn1tkpur93x38n(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_y2xvmwbn1tkpur93x38n, self).__init__(filename="y2xvmwbn1tkpur93x38n.raw")


class BombermanEnv_y59h2rius6go0ufo9gss(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_y59h2rius6go0ufo9gss, self).__init__(filename="y59h2rius6go0ufo9gss.raw")


class BombermanEnv_z0e51drhgjksoqofwjac(BombermanEnv):

    def __init__(self):
        super(BombermanEnv_z0e51drhgjksoqofwjac, self).__init__(filename="z0e51drhgjksoqofwjac.raw")
