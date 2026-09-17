import numpy as np
L=.05;A=.03;D=.07;N=100e6
tl=min(max(L-A,0),D-A)/(D-A)
assert tl==.5
assert np.isclose(tl*(D-A)*N,2e6)
assert min(max(.02-A,0),D-A)==0
print('22.4 checked',tl)
