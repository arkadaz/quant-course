import numpy as np
kappa=.636905;theta=.044816;sigma=.002887
half=np.log(2)/kappa
assert np.isclose(half,1.0884,atol=.03) and 2*kappa*theta > sigma**2
print('20.5 checked',half,2*kappa*theta,sigma**2)
