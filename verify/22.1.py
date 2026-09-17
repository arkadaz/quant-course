import numpy as np
B0=400000.;r=.06/12;N=360;A=B0*r/(1-(1+r)**-N)
B12=B0*(1+r)**12-A*((1+r)**12-1)/r
assert np.isclose(A,2398.2021,rtol=0,atol=.01)
assert np.isclose(B12,395087.95,rtol=0,atol=.02)
assert np.isclose(r*B0,2000.)
assert np.isclose(A-r*B0,398.2021,rtol=0,atol=.01)
print('22.1 checked',A,B12)
