import numpy as np
bid=np.array([12.5,6.3,2.4]);ask=np.array([12.9,6.5,2.6]);model=np.array([12.66,6.43,2.48])
mid=.5*(bid+ask);h=.5*(ask-bid);res=(model-mid)/h
assert np.allclose(res,[-.2,.3,-.2])
assert np.isclose(.5*np.sum(res*res),.085)
assert np.all((model>=bid)&(model<=ask))
print('21.4 checked')
