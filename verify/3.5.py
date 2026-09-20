import numpy as np
from scipy.stats import norm
sr,T=1.2,3
tstat=sr*np.sqrt(T)
se=np.sqrt((1+.5*sr**2)/T)
assert np.isclose(tstat,2.0784609691)
assert np.isclose(2*(1-norm.cdf(tstat)),.0376669222)
assert np.isclose(se,.7571877794)
assert np.isclose(sr-1.96*se,-.2840880477)
assert np.isclose(sr+1.96*se,2.6840880477)
assert np.isclose((3/sr)**2,6.25)
assert np.isclose(np.sqrt((1+.5)/(1-.5)),np.sqrt(3))
