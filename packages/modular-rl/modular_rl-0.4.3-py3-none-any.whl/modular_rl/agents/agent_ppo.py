
# -*- coding: utf-8 -*-
"""
ModularRL project

Copyright (c) 2023 horrible

Class AgentPPO is an implementation of the Proximal Policy Optimization (PPO) algorithm. 
It takes an environment and a setting configuration as inputs, initializes neural network instances and optimizers, 
and sets various learning parameters. 
It has methods to predict an action given a state, perform a learning step, update the neural network parameters, 
save and load a checkpoint, and reset learning parameters. 
The class also has instance variables to keep track of episode and total rewards, previous reward, and average reward.

This software includes the following third-party libraries:
Gym (MIT License): https://github.com/openai/gym - Copyright (c) OpenAI.
NumPy (BSD License): https://numpy.org - Copyright (c) NumPy Developers.
PyTorch  (BSD-Style License): https://pytorch.org/ - Copyright (c) Facebook.
"""

import gym
from modular_rl.networks import PolicyNetwork, ValueNetwork
import torch.optim as optim
import torch
from torch.distributions import Categorical
import numpy as np


class AgentPPO:
    def __init__(self, env, setting):
        """
        Initialize the AgentPPO class with the specified environment and settings.

        :param env: The environment to use for training.
        :type env: gym.Env or None
        :param setting: The settings for the PPO algorithm.
        :type setting: AgentSettings
        """
        # Environment preparation
        self.env = env if env else gym.make('CartPole-v0')
        self.setting = setting
        self.state_dim = self.env.observation_space.shape[0]
        self.action_dim = self.env.action_space.n

        # Create neural network instances and optimizer
        self.policy_net = PolicyNetwork(
            self.state_dim, self.action_dim, setting.get('networks', 'middle'))
        self.value_net = ValueNetwork(
            self.state_dim, setting.get('networks', 'middle'))
        self.policy_optimizer = optim.Adam(
            self.policy_net.parameters(), lr=setting.get('optimizer_speed', 3e-4))
        self.value_optimizer = optim.Adam(
            self.value_net.parameters(), lr=setting.get('optimizer_speed', 3e-4))

        # Set learning parameters
        self.max_episodes = setting.get('max_episodes', 30)
        self.max_timesteps = setting.get('max_timesteps', 200)
        self.update_timestep = setting.get('update_timestep', 2000)
        self.ppo_epochs = setting.get('ppo_epochs', 4)
        self.mini_batch_size = setting.get('mini_batch_size', 64)
        self.gamma = setting.get('gamma', 0.99)
        self.lam = setting.get('lam', 0.95)
        self.clip_param = setting.get('clip_param', 0.2)
        self.early_stop_threshold = setting.get('early_stop_threshold', -1)
        self.done_loop_end = setting.get('done_loop_end', False)
        self.reward_print = setting.get('reward_print', True)

        # Set learn episode parameters
        self.episode_reward = 0
        self.total_reward = 0
        self.prev_reward = 0
        self.episode = 0
        self.avg_reward = 0

        # Set learn modular parameters
        self.state = None
        self.dist = None

    # Implement PPO algorithm
    def compute_advantages(self, rewards, values, done, gamma=0.99, lam=0.95):
        """
        Compute advantages given the rewards, values, done flags, and discount factors.

        :param rewards: The rewards obtained from the environment.
        :type rewards: numpy.ndarray
        :param values: The predicted state-value from the critic network.
        :type values: numpy.ndarray
        :param done: The done flags obtained from the environment.
        :type done: numpy.ndarray
        :param gamma: The discount factor.
        :type gamma: float
        :param lam: The GAE lambda value.
        :type lam: float
        :return: The calculated advantages.
        :rtype: numpy.ndarray
        """

        advantages = np.zeros_like(rewards)
        last_advantage = 0
        for t in reversed(range(len(rewards))):
            delta = rewards[t] + gamma * \
                values[t + 1] * (1 - done[t]) - values[t]
            advantages[t] = delta + gamma * lam * \
                last_advantage * (1 - done[t])
            last_advantage = advantages[t]
        return advantages

    def ppo_iter(self, mini_batch_size, states, actions, log_probs, returns, advantages):
        """
        Generate random mini-batches of data for PPO algorithm.

        :param mini_batch_size: The size of each mini-batch.
        :type mini_batch_size: int
        :param states: The states from the environment.
        :type states: torch.Tensor
        :param actions: The actions taken in the environment.
        :type actions: torch.Tensor
        :param log_probs: The logarithmic probabilities of the actions.
        :type log_probs: torch.Tensor
        :param returns: The calculated returns.
        :type returns: torch.Tensor
        :param advantages: The calculated advantages.
        :type advantages: torch.Tensor
        :yield: A mini-batch of data.
        """

        batch_size = states.size(0)
        for _ in range(batch_size // mini_batch_size):
            rand_ids = np.random.randint(0, batch_size - 1, mini_batch_size)
            yield states[rand_ids, :], actions[rand_ids], log_probs[rand_ids], returns[rand_ids], advantages[rand_ids]

    def ppo_update(self, ppo_epochs, mini_batch_size, states, actions, log_probs, returns, advantages, clip_param=0.2):
        """
        Perform PPO algorithm for the specified number of epochs.

        :param ppo_epochs: The number of epochs to run PPO algorithm.
        :type ppo_epochs: int
        :param mini_batch_size: The size of each mini-batch.
        :type mini_batch_size: int
        :param states: The states from the environment.
        :type states: torch.Tensor
        :param actions: The actions taken in the environment.
        :type actions: torch.Tensor
        :param log_probs: The logarithmic probabilities of the actions.
        :type log_probs: torch.Tensor
        :param returns: The calculated returns.
        :type returns: torch.Tensor
        :param advantages: The calculated advantages.
        :type advantages: torch.Tensor
        :param clip_param: The PPO clipping parameter.
        :type clip_param: float
        """

        for _ in range(ppo_epochs):
            for state, action, old_log_probs, return_, advantage in self.ppo_iter(mini_batch_size, states, actions, log_probs, returns, advantages):
                dist = Categorical(self.policy_net(state))
                new_log_probs = dist.log_prob(action)

                ratio = (new_log_probs - old_log_probs).exp()
                surr1 = ratio * advantage
                surr2 = torch.clamp(ratio, 1.0 - clip_param,
                                    1.0 + clip_param) * advantage
                policy_loss = -torch.min(surr1, surr2).mean()

                value_loss = (return_ - self.value_net(state)).pow(2).mean()
                self.value_optimizer.zero_grad()
                value_loss.backward()
                self.value_optimizer.step()

    def select_action(self, state):
        """
        Selects an action based on the given state and the current policy.

        :param state: The state to use for selecting an action.
        :type state: numpy.ndarray
        :return: The selected action and its corresponding probability distribution.
        :rtype: tuple(torch.Tensor, torch.distributions.Categorical)
        """

        state = self._check_state(self.state)
        state_tensor = torch.tensor(state, dtype=torch.float32)
        with torch.no_grad():
            action_probs = self.policy_net(state_tensor)
        dist = Categorical(action_probs)
        self.dist = dist
        action = dist.sample()
        return action, dist

    def learn_step(self, state, timestep):
        """
        Takes a step in the environment and updates the PPO algorithm with the resulting state, reward, and action.

        :param state: The current state of the environment.
        :type state: numpy.ndarray
        :param timestep: The current timestep of the training process.
        :type timestep: int
        :return: The action taken, the resulting reward, and whether the episode is done or not.
        :rtype: tuple(torch.Tensor, float, bool)
        """

        action, dist = self.select_action(state)

        return self.update_step(state, dist, action, timestep)

    def update_step(self, state, dist, action, timestep):
        """
        Takes a step in the environment with a given action and updates the PPO algorithm with the resulting state, reward, and action.

        :param state: The current state of the environment.
        :type state: numpy.ndarray
        :param dist: The corresponding probability distribution.
        :type dist: torch.distributions.Categorical
        :param action: The action taken by the agent.
        :type action: int
        :param reaction: The reaction of the opponent after the agent's action.
        :type reaction: tuple
        :param timestep: The current timestep of the training process.
        :type timestep: int
        :return: The resulting reward and whether the episode is done or not.
        :rtype: tuple(float, bool)
        """

        if dist == None and self.dist:
            dist = self.dist

        step_output = self.env.step(action.item())
        step_output_num = len(step_output)

        if step_output_num == 4:
            next_state, reward, is_done, _ = self.env.step(action.item())
        elif step_output_num == 5:
            next_state, reward, is_done, _, _ = self.env.step(action.item())

        self.episode_reward += reward
        self.total_reward += reward
        self.prev_reward = reward

        state = self._check_state(state)

        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        self.next_states.append(next_state)
        self.done.append(is_done)
        self.log_probs.append(dist.log_prob(action))

        self.state = next_state

        if timestep > 0:
            timestep += 1

        if self.update_timestep > 0 and timestep > 0 and (timestep % self.update_timestep == 0):
            self.update()

        return action, reward, is_done

    def update(self):
        """
        Perform an update of the PPO algorithm, using the stored information about the environment from the previous learning iterations.
        """
        states_tensor = torch.tensor(np.array(self.states, dtype=np.float32))
        actions_tensor = torch.tensor(np.array(self.actions))
        rewards_tensor = torch.tensor(np.array(self.rewards, dtype=np.float32))
        next_states_tensor = torch.tensor(
            np.array(self.next_states, dtype=np.float32))
        done_tensor = torch.tensor(np.array(self.done, dtype=np.float32))
        log_probs_tensor = torch.stack(self.log_probs)

        values = self.value_net(states_tensor).detach().squeeze()
        next_values = self.value_net(next_states_tensor).detach().squeeze()

        advantages = self.compute_advantages(rewards_tensor.numpy(), np.append(
            values.numpy(), next_values[-1].item()), done_tensor.numpy(), self.gamma, self.lam)
        advantages = (advantages - advantages.mean()) / \
            (advantages.std() + 1e-5)
        advantages_tensor = torch.tensor(advantages, dtype=torch.float32)

        returns = np.add(advantages[:-1], values[:-1])
        self.ppo_update(self.ppo_epochs, self.mini_batch_size, states_tensor,
                        actions_tensor, log_probs_tensor, returns, advantages_tensor)

        self.reset()

        self.episode += 1
        self.episode_reward = 0

    def learn(self):
        """
        Execute the learning loop, where the PPO algorithm is used to train the agent on the specified environment.
        """

        timestep = 0
        test = 0
        self.total_reward = 0
        self.episode_reward = 0

        if self.max_episodes > 0 and self.max_timesteps > 0:
            is_done = False
            for episode in range(self.max_episodes):
                self.reset()
                self.learn_reset()
                reward = 0

                for t in range(self.max_timesteps):
                    _, reward, is_done = self.learn_step(self.state, timestep)
                    if is_done:
                        break

                self.total_reward += self.episode_reward

                avg_reward = self.total_reward / (episode + 1)
                if self.reward_print:
                    print(
                        f'Episode: {episode}, Episode Reward: {self.episode_reward}, Total Reward: {self.total_reward}, Average Reward: {avg_reward}')

                if avg_reward >= self.early_stop_threshold > 0:
                    if self.reward_print:
                        print(
                            f'Early stopping: Average reward has reached the threshold ({self.early_stop_threshold}) at episode {episode}')
                    break
                if is_done and self.done_loop_end:
                    break

                if episode + 1 >= self.max_episodes:
                    break

            self.env.close()
        else:
            self.reset()

    def reset(self):
        """
        Reset the lists that contain information about the states, actions, rewards, and other values for the agent.
        """

        self.states = []
        self.actions = []
        self.rewards = []
        self.next_states = []
        self.done = []
        self.log_probs = []

    def learn_reset(self):
        """
        Reset the agent's state and episode reward.
        """

        self.state = self.env.reset()

        return self._check_state(self.state)

    def learn_next(self):
        """
        Perform a single learning step and update the episode and total rewards.

        :return: The action taken, the resulting reward, and whether the episode is done or not.
        :rtype: tuple(torch.Tensor, float, bool)
        """

        action, reward, is_done = self.learn_step(self.state, -1)

        return action, reward, is_done

    def learn_close(self):
        """
        Close the environment and reset the agent's total reward, episode count, and episode reward.
        """

        self.env.close()
        self.total_reward = 0
        self.episode = 0
        self.episode_reward = 0

    def learn_check(self):
        """
        Print the episode count, previous reward, episode reward, total reward, and average episode reward.
        """

        avg_reward = self.total_reward / (self.episode + 1)
        if self.reward_print:
            print(
                f'Episode: {self.episode}, Previous Reward: {self.prev_reward},  Episode Reward: {self.episode_reward}, Total Reward: {self.total_reward}, Average Episode Reward: {avg_reward}')

    def _check_state(self, state):
        state_num = len(state)
        if state_num == 2:
            state, _ = state  # Unpack the tuple
        return state

    def save(self, file_name):
        """
        Initialize the AgentPPO class with the specified environment and settings.

        :param env: The environment to use for training.
        :type env: gym.Env or None
        :param setting: The settings for the PPO algorithm.
        :type setting: AgentSettings
        """

        torch.save({
            'policy_net_state_dict': self.policy_net.state_dict(),
            'value_net_state_dict': self.value_net.state_dict(),
            'policy_optimizer_state_dict': self.policy_optimizer.state_dict(),
            'value_optimizer_state_dict': self.value_optimizer.state_dict(),
        }, file_name)

    def load(self, file_name):
        """
        Compute advantages for the PPO algorithm.

        :param rewards: The rewards.
        :type rewards: numpy.ndarray
        :param values: The values.
        :type values: numpy.ndarray
        :param done: The done signals.
        :type done: numpy.ndarray
        :param gamma: The discount factor.
        :type gamma: float
        :param lam: The lambda parameter.
        :type lam: float
        :return: The computed advantages.
        :rtype: numpy.ndarray
        """

        checkpoint = torch.load(file_name)
        self.policy_net.load_state_dict(checkpoint['policy_net_state_dict'])
        self.value_net.load_state_dict(checkpoint['value_net_state_dict'])
        self.policy_optimizer.load_state_dict(
            checkpoint['policy_optimizer_state_dict'])
        self.value_optimizer.load_state_dict(
            checkpoint['value_optimizer_state_dict'])
