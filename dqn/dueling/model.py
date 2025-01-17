import torch
import torch.nn as nn
import torch.nn.functional as F

class DuelQNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(DuelQNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fp1 = nn.Linear(state_size, 128)
        self.fp2 = nn.Linear(128, 256)
        self.head_values = nn.Linear(256, 1)
        self.head_advantages = nn.Linear(256, action_size)


    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fp1(state))
        x = F.relu(self.fp2(x))
        values = self.head_values(x)
        advantages = self.head_advantages(x)
        return values + (advantages - advantages.mean())
