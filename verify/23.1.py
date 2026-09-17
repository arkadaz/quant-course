import numpy as np
q=(1.05-.8)/(1.4-.8)
cu=(q*10.6+(1-q)*2.2)/1.05
cd=(q*2.2)/1.05
v0=(q*cu+(1-q)*cd)/1.05
assert np.isclose(q,5/12) and np.isclose(cu,5.4285714) and np.isclose(cd,.8730159)
assert np.isclose(v0,2.6392038)
print('23.1 checked',q,v0)
