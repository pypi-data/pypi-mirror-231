from ..templates import Layer
from ..core import DeeplayModule
from ..config import Config, Ref

import torch
import torch.nn as nn

__all__ = ["Skip", "Concatenate", "Add"]


class Skip(DeeplayModule):
    defaults = Config().inputs[0](nn.Identity)

    def __init__(self, inputs, func):
        """Skip module.

        Parameters
        ----------
        inputs : list of Layer
            List of inputs.
        func : callable
            Function to apply to the inputs.
        """

        super().__init__(inputs=inputs, func=func)

        self.func = self.attr("func")
        self.inputs = self.new("inputs")

    def forward(self, x):
        inputs = [inp(x) for inp in self.inputs]
        return self.func(*inputs)


class Concatenate(DeeplayModule):
    defaults = Config().merge(None, Skip.defaults).dim(1)

    def __init__(self, inputs, dim=1):
        """Concatenate module.

        Parameters
        ----------
        inputs : list of Layer
            List of inputs.
        dim : int
            Dimension to concatenate on.
            Default is 1.
        """

        super().__init__(inputs=inputs, dim=dim)

        self.dim = self.attr("dim")
        self.inputs = self.new("inputs")

    def forward(self, x):
        inputs = [inp(x) for inp in self.inputs]
        return torch.cat(inputs, dim=self.dim)


class Add(Skip):
    defaults = Config().merge(None, Skip.defaults)

    def __init__(self, inputs):
        """Add module.

        Parameters
        ----------
        inputs : list of Layer
            List of inputs.
        """

        super().__init__(inputs=inputs)

        self.inputs = self.new("inputs")

    def forward(self, x):
        inputs = [inp(x) for inp in self.inputs]
        return sum(inputs)
