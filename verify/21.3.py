import numpy as np
from scipy.stats import norm
S=100.;K=100.;r=.05;sig=.2;T=1.
d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
c=S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
assert np.isclose(c,10.450583572185565)
assert np.isclose(2*np.pi/(4096*.25),.006135923151542565)
print('21.3 checked')
