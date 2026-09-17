import numpy as np
loss=.0848964603;ann=4.2448318563
pv=1e7*.6*loss;spread=.6*loss/ann;value=pv-1e7*.0125*ann
assert np.isclose(pv,509378.76,atol=.01) and np.isclose(spread,.011999975,atol=1e-9)
assert np.isclose(value,-21225.22,atol=.01)
print('20.7 checked',pv,spread,value)
