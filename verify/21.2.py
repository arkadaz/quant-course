import numpy as np
r=np.array([-.5,1.,-.2]);J=10*np.eye(3);lam=25
delta=np.linalg.solve(J.T@J+lam*np.eye(3),-J.T@r)
assert np.allclose(delta,[.04,-.08,.016])
assert np.isclose(.5*np.sum(r*r),.645)
r_new=r+J@delta
assert np.isclose(.5*np.sum(r_new*r_new),.0258)
print('21.2 checked')
