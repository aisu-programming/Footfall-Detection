import torch
import torch.nn as nn

class MishCuda(nn.Module):
    def forward(self, x):
            return x * torch.nn.functional.softplus(x).tanh()