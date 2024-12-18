import numpy as np
import pandas as pd
import scipy
from scipy import sparse

import numpy as np
from scipy.sparse import csr_matrix


def define_test_input(args):
    if args.test_case == 1:
        arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    elif args.test_case == 2:
        np.random.seed(42)
        arr = np.random.rand(6, 6)
    return arr


def ans1(_a):
    arr = _a
    M = csr_matrix(arr)
    result = M.A.diagonal(0)
    return result


if __name__ == "__main__":
    import argparse
    import os
    import pickle

    parser = argparse.ArgumentParser()
    parser.add_argument("--test_case", type=int, default=1)
    args = parser.parse_args()

    a = define_test_input(args)
    ans = ans1(a)

    if not os.path.exists("input"):
        os.mkdir("input")
    with open("input/input{}.pkl".format(args.test_case), "wb") as f:
        pickle.dump(a, f)

    if not os.path.exists("ans"):
        os.mkdir("ans")
    with open("ans/ans{}.pkl".format(args.test_case), "wb") as f:
        pickle.dump(ans, f)
