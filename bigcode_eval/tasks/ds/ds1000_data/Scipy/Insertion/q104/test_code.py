import numpy as np
import pandas as pd
import io
from scipy import integrate, signal


def test(result, ans):
    np.testing.assert_array_equal(result, ans)
    return 1
