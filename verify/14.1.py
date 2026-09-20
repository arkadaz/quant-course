import numpy as np
from scipy.stats import norm
S,K,r,sig,tau=100.0,105.0,0.04,0.20,0.25
d1=(np.log(S/K)+(r+0.5*sig**2)*tau)/(sig*np.sqrt(tau));d2=d1-sig*np.sqrt(tau)
C=S*norm.cdf(d1)-K*np.exp(-r*tau)*norm.cdf(d2)
delta=norm.cdf(d1);gamma=norm.pdf(d1)/(S*sig*np.sqrt(tau))
theta=-S*norm.pdf(d1)*sig/(2*np.sqrt(tau))-r*K*np.exp(-r*tau)*norm.cdf(d2)
B=C-S*delta
residual=theta+r*S*delta+0.5*sig**2*S**2*gamma-r*C
assert np.isclose(C,2.3908769614699386)
assert np.isclose(delta,0.36771865542601334)
assert np.isclose(gamma,0.037680506505494295)
assert np.isclose(theta,-8.911340846318136)
assert np.isclose(B,-34.380988581131396)
assert abs(residual)<1e-11
assert np.isclose(S*delta+B,C)
