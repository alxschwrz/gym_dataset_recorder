import pandas as pd
import csv


def reset_data():
    return {'observations': [],
            'actions': [],
            'terminals': [],
            'rewards': [],
            #'infos/goal': [],
            #'infos/task': [],
            #'infos/qpos': [],
            #'infos/qvel': [],
            }

def append_data(data, s, a, tgt, done, env_data):
    data['observations'].append(s)
    data['actions'].append(a)
    data['rewards'].append(0.0)
    data['terminals'].append(done)
    #data['infos/goal'].append(tgt)
    #data['infos/qpos'].append(env_data.qpos.ravel().copy())
    #data['infos/qvel'].append(env_data.qvel.ravel().copy())


def store_data(data, filename='data.csv'):
    df = pd.DataFrame.from_dict(data)
    df.to_csv(filename)
