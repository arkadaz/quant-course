import numpy as np
A=.9512+.9048+.8600+.8170+.7760
s=(1-.7760)/A
v=50e6*(.0525-s)*A
assert np.isclose(A,4.309) and np.isclose(s,.051984219,atol=1e-9)
assert np.isclose(v,111125) and np.isclose(50e6*A*1e-4,21545)
print('20.2 checked',A,s,v)
