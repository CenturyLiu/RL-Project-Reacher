#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:55:58 2020

@author: centuryliu
"""



from unityagents import UnityEnvironment
import numpy as np
from collections import namedtuple, deque
from ddpg_agent import Agent
import matplotlib.pyplot as plt
import torch
import random

env = UnityEnvironment(file_name='/home/centuryliu/reinforcement_learning/deep-reinforcement-learning/p2_continuous-control/ddpg_multiple/Reacher_Linux/Reacher.x86_64')


# get the default brain
brain_name = env.brain_names[0]
brain = env.brains[brain_name]

# reset the environment
env_info = env.reset(train_mode=True)[brain_name]

# number of agents
num_agents = len(env_info.agents)
print('Number of agents:', num_agents)

# size of each action
action_size = brain.vector_action_space_size
print('Size of each action:', action_size)

# examine the state space 
states = env_info.vector_observations
state_size = states.shape[1]
print('There are {} agents. Each observes a state with length: {}'.format(states.shape[0], state_size))
print('The state for the first agent looks like:', states[0])


agent = Agent(state_size = state_size, action_size = action_size, random_seed=2, num_agents = num_agents)
 
agent.actor_local.load_state_dict(torch.load('checkpoint_actor.pth'))
agent.actor_target.load_state_dict(torch.load('checkpoint_actor.pth'))
agent.critic_local.load_state_dict(torch.load('checkpoint_critic.pth'))
agent.critic_target.load_state_dict(torch.load('checkpoint_critic.pth'))

def watch(n_episodes=1, max_t=1000):
    scores_deque = deque(maxlen=100)
    scores = []
    for i_episode in range(1,n_episodes + 1):
        brain_name = env.brain_names[0]
        brain = env.brains[brain_name]
        # reset the environment and get initial observation
        env_info = env.reset(train_mode=False)[brain_name]
        states = env_info.vector_observations
        # reset the agent
        agent.reset()
        score = np.zeros(num_agents)
        for t in range(max_t):
            action = agent.act(states)
            
            #print(action)
            
            env_info = env.step(action)[brain_name]
            next_states = env_info.vector_observations
            rewards = env_info.rewards
            dones = env_info.local_done
            score += rewards
            #for i in range(num_agents):
            #    agent.step(states[i], action[i], rewards[i], next_states[i], dones[i], t)
            states = next_states
            
            if np.any(dones):
                break
        score = score.mean()
        scores_deque.append(score)
        scores.append(score)
        print('\rEpisode {}\tAverage Score: {:.2f}\tScore: {:.2f}'.format(i_episode, np.mean(scores_deque), score), end="")
        if i_episode % 100 == 0:
            print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
        if np.mean(scores_deque)>=30.0:
            print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores_deque)))
            torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
            torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')
            break
    return scores

scores = watch()

env.close()
        
        
        

        
