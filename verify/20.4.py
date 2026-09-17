import numpy as np
q=np.array([.236621287,.475620657,.238999370]);r=np.array([.07,.05,.03]);disc=np.exp(-r*.5);cap=1e7*.5*np.maximum(r-.0525,0);floor=1e7*.5*np.maximum(.0525-r,0)
assert np.isclose(q@(disc*cap),19992.24,atol=.01) and np.isclose(q@(disc*floor),32285.60,atol=.01)
print('20.4 checked',q@(disc*cap),q@(disc*floor))
