from mnist import MNISTBandit
from fashionmnist import FashionMNISTBandit
from cifar10 import CIFAR10Bandit
from onedbandit import OneDBandit
from onehotbandit import OneHotBandit
from bsuite.utils import gym_wrapper

env = MNISTBandit()
gym_env = gym_wrapper.GymFromDMEnv(env)
gym_env.reset()

T = 100

for i in range(T):
    _, rew, done, info = gym_env.step(gym_env.action_space.sample())
    if i%25==0:
        print("reward: ", rew)
    if done:
        obs = gym_env.reset()


env = FashionMNISTBandit()
gym_env = gym_wrapper.GymFromDMEnv(env)
gym_env.reset()

for i in range(T):
    _, rew, done, info = gym_env.step(gym_env.action_space.sample())
    if i%25==0:
        print("reward: ", rew)
    if done:
        obs = gym_env.reset()


env = CIFAR10Bandit()
gym_env = gym_wrapper.GymFromDMEnv(env)
gym_env.reset()

for i in range(T):
    _, rew, done, info = gym_env.step(gym_env.action_space.sample())
    if i%25==0:
        print("reward: ", rew)
    if done:
        obs = gym_env.reset()

env = OneDBandit()
gym_env = gym_wrapper.GymFromDMEnv(env)
gym_env.reset()

for i in range(T):
    _, rew, done, info = gym_env.step(gym_env.action_space.sample())
    if i%25==0:
        print("reward: ", rew)
    if done:
        obs = gym_env.reset()

env = OneHotBandit()
gym_env = gym_wrapper.GymFromDMEnv(env)
gym_env.reset()

for i in range(T):
    _, rew, done, info = gym_env.step(gym_env.action_space.sample())
    if i%25==0:
        print("reward: ", rew)
    if done:
        obs = gym_env.reset()