#!/usr/bin/env python

import sys
import numpy as np
import scipy as sp
import sklearn

if __name__ == "__main__":
    print('Hello, Conda!')

    print("Python: {}".format(sys.version))
    print("NumPy: {}".format(np.__version__))
    print("SciPy: {}".format(sp.__version__))
    print("scikit-learn: {}".format(sklearn.__version__))