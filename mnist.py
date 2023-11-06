"""MNIST classification as a bandit.

Adapted from https://github.com/google-deepmind/bsuite/tree/main/bsuite
"""

from bsuite.environments import base
from bsuite.experiments.mnist import sweep
from datasets import load_mnist

import dm_env
from dm_env import specs
import numpy as np


class MNISTBandit(base.Environment):
  """MNIST classification as a bandit environment."""

  def __init__(self, fraction: float = 1., seed: int = None):
    """Loads the MNIST training set (60K images & labels) as numpy arrays.

    Args:
      fraction: What fraction of the training set to keep (default is all).
      seed: Optional integer. Seed for numpy's random number generator (RNG).
    """
    super().__init__()
    (images, labels), _ = load_mnist()

    num_data = len(labels)

    self._num_data = int(fraction * num_data)
    self._image_shape = images.shape[1:]

    self._images = images[:self._num_data]
    self._labels = labels[:self._num_data]
    self._rng = np.random.RandomState(seed)
    self._correct_label = None

    self._total_regret = 0.
    self._optimal_return = 1.

    self.bsuite_num_episodes = sweep.NUM_EPISODES

  def _reset(self) -> dm_env.TimeStep:
    """Agent gets an MNIST image to 'classify' using its next action."""
    idx = self._rng.randint(self._num_data)
    image = self._images[idx].astype(np.float32) / 255
    self._correct_label = self._labels[idx]

    return dm_env.restart(observation=image)

  def _step(self, action: int) -> dm_env.TimeStep:
    """+1/-1 for correct/incorrect guesses. This also terminates the episode."""
    correct = action == self._correct_label
    reward = 1. if correct else -1.
    self._total_regret += self._optimal_return - reward
    observation = np.zeros(shape=self._image_shape, dtype=np.float32)
    return dm_env.termination(reward=reward, observation=observation)

  def observation_spec(self):
    return specs.Array(shape=self._image_shape, dtype=np.float32)

  def action_spec(self):
    return specs.DiscreteArray(num_values=10)

  def bsuite_info(self):
    return dict(total_regret=self._total_regret)