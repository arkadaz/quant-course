import numpy as np
from scipy.stats import t
assert np.isclose(1.96*.20, .392)
assert np.isclose(.08-1.96*.20, -.312)
assert np.isclose(.08+1.96*.20, .472)
critical=t.ppf(.975,3)
assert np.isclose(critical, 3.1824463053)
half=critical*.20/np.sqrt(4)
assert np.isclose(half, .3182446305)
assert np.isclose(.08-half, -.2382446305)
assert np.isclose(.08+half, .3982446305)
