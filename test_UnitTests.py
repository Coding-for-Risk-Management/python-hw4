import numpy as np

import TMat1
def test_TMAT1():
    rLast = np.repeat(['A', 'B', 'C'], [3, 4, 5])
    rNow = np.repeat(['A', 'B', 'C'], [5, 2, 5])
    
    out = TMat1.TMAT1(rLast, rNow)
    answer = np.array([1, 0, 0, 0.5, 0.5, 0, 0, 0, 1]).reshape(3, 3)
    assert np.array_equal(out, answer)
