import gym
import generate_dataset as gd


def main():
    env = gym.make('MountainCarContinuous-v0')
    observation = env.reset()
    data = gd.reset_data()
    for t in range(105):
        env.render()
        #print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        gd.append_data(data, observation, action, 0, done, None)
        #print(observation, reward, done, info)
        if done:
            print("Finished after {} timesteps".format(t + 1))
            break
    gd.store_data(data)


if __name__ == "__main__":
    main()
