import numpy as np
q=.5;qu=.5*np.exp(-.05*.5);qm=qu*(1-q)*np.exp(-.06*.5)+qu*q*np.exp(-.04*.5);quu=qu*q*np.exp(-.06*.5);qdd=qu*(1-q)*np.exp(-.04*.5)
p=np.exp(-np.array([.07,.05,.03])*.5);pay=1e6*np.maximum(p-.975,0);v=quu*pay[0]+qm*pay[1]+qdd*pay[2]
assert np.isclose(qu,.487654956,atol=1e-9) and np.isclose(quu+qm+qdd,.951241315,atol=1e-9)
assert np.isclose(v,2564.15,atol=.01)
print('20.3 checked',v)
