import numpy as np
ltv=465000/400000;lgd=85000/465000
assert np.isclose(ltv,1.1625)
assert np.isclose(lgd,.1827957,atol=1e-7)
V=95e6;D=95e6;h=.15;gap=D-(1-h)*V
assert np.isclose(gap,14.25e6)
print('22.5 checked',ltv,lgd,gap)
