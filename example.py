import gym
import generate_dataset as gd


def main():
    env = gym.make('MountainCar-v0')
    observation = env.reset()
    recorder = gd.DatasetGenerator(goal=False)
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        recorder.append_data(observation, action, reward, done, info)
        if done:
            print("Finished after {} timesteps".format(t + 1))
            break
    recorder.write_data(filename='recorded_data.csv')
    recorder.reformat_data_next_obs()
    recorder.write_data(filename='recorded_data_next_obs.csv')


if __name__ == "__main__":
    main()
