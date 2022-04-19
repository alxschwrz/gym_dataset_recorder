import pandas as pd
import numpy as np


class DatasetGenerator(object):
    def __init__(self, goal=False, observationSpaceType="array"):
        self.goal = goal
        self.data = self._reset_data()
        self._num_samples = 0
        self._observationSpaceType = observationSpaceType

    def _reset_data(self):
        data = {'observations': [],
                'actions': [],
                'terminals': [],
                'rewards': [],
                'infos': [],
                }
        if self.goal:
            data['goal'] = []
        return data

    def __len__(self):
        return self._num_samples

    def append_data(self, s, a, rew, done, info, goal=None):
        self._num_samples += 1
        self.data['observations'].append(s)
        self.data['actions'].append(a)
        self.data['terminals'].append(done)
        self.data['rewards'].append(rew)
        self.data['infos'].append(info)
        if self.goal:
            self.data['goal'].append(goal)

    def reformat_data_next_obs(self):
        self.data['next_observations'] = self.data['observations'][1:]
        if self._observationSpaceType == "array":
            self.data['next_observations'].append(np.zeros(self.data['observations'][0].shape)) # last element has no next observation
        elif self._observationSpaceType == "dict":
            last_row = self.data['observations'][0]
            for key in last_row:
                last_row[key][:] = 0
            self.data['next_observations'].append(last_row)


    def write_data(self, filename='recorded_data_templatename', filetype="pickle"):
        print('writing dataset to file ...')
        df = pd.DataFrame.from_dict(self.data)
        df.to_csv(filename+'.csv')
        print('dataset saved as {}'.format(filename+'.csv'))
        df.to_pickle(filename+'.pkl')
        print('dataset saved as {}'.format(filename+'.pkl'))


