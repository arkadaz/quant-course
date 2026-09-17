import numpy as np
q=np.exp(-.018*5);f=1-q
pv=2077689.22+7297888.74+308812.72
assert np.isclose(q,.913931,atol=1e-6) and np.isclose(f,.086069,atol=1e-6)
assert np.isclose(pv,9684390.68) and np.isclose(.018*.6,.0108)
print('20.6 checked',q,f,pv)
