import numpy as np
from scipy.stats import norm
S,K,r,sig,T=100.0,105.0,0.04,0.20,0.25
d1=(np.log(S/K)+(r+0.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
D=np.exp(-r*T);C=S*norm.cdf(d1)-K*D*norm.cdf(d2);P=K*D*norm.cdf(-d2)-S*norm.cdf(-d1)
assert np.isclose(d1,-0.33790164169432065)
assert np.isclose(d2,-0.43790164169432064)
assert np.isclose(norm.cdf(d1),0.36771865542601334)
assert np.isclose(norm.cdf(d2),0.33072879268924665)
assert np.isclose(D,0.9900498337491681)
assert np.isclose(C,2.3908769614699386)
assert np.isclose(P,6.346109505132589)
assert np.isclose(C-P,S-K*D)
assert max(S-K*D,0)<=C<=S
assert np.isclose(100*C,239.08769614699385)
