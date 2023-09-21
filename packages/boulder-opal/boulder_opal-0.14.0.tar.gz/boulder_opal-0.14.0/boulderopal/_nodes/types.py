from typing import Union

import numpy as np

from .node_data import (
    Pwc,
    Stf,
    Tensor,
)

TensorLike = Union[np.ndarray, Tensor]
TensorLikeOrFunction = Union[np.ndarray, Tensor, Pwc, Stf]
NumericOrFunction = Union[float, complex, np.ndarray, Tensor, Pwc, Stf]
_IntType = (int, np.integer)
