import numpy as np
from scipy.stats import norm
S,K,T,r,q,Cm,Pm,m=5000.0,5000.0,0.5,0.04,0.015,300.0,235.0,100.0
A=S*np.exp(-q*T);B=K*np.exp(-r*T);F=S*np.exp((r-q)*T);eps=(Cm-Pm)-(A-B)
assert np.isclose(A,4962.640273724912)
assert np.isclose(B,4900.993366533777)
assert np.isclose(A-B,61.646907191134815)
assert np.isclose(eps,3.3530928088651852)
assert np.isclose(m*eps,335.3092808865185)
for ST in [3500.0,5000.0,6500.0]:
 assert np.isclose(max(ST-K,0)-max(K-ST,0),ST-K)
 assert np.isclose(-max(ST-K,0)+max(K-ST,0)+ST-K,0)
for sig in [0.1,0.2,0.5]:
 d1=(np.log(S/K)+(r-q+0.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
 c=S*np.exp(-q*T)*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
 p=K*np.exp(-r*T)*norm.cdf(-d2)-S*np.exp(-q*T)*norm.cdf(-d1)
 assert np.isclose(c-p,A-B)
