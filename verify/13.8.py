import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
F,r,T,s=5000.0,0.04,30/365,0.20
D=np.exp(-r*T)
def black(K,put=False):
    d1=(np.log(F/K)+0.5*s*s*T)/(s*np.sqrt(T));d2=d1-s*np.sqrt(T)
    c=D*(F*norm.cdf(d1)-K*norm.cdf(d2))
    return c-D*(F-K) if put else c
ks=np.arange(3000,7001,50.0)
q=np.array([black(k,put=k<F) for k in ks])
strip=np.sum(50*q/ks**2)
kvar=2*np.exp(r*T)*strip/T
assert np.isclose(D,0.9967177272404354)
assert np.isclose(black(5000),113.98217879207559)
assert np.isclose(strip,0.0016467458313724381)
assert np.isclose(kvar,0.04020277169244778)
assert np.isclose(np.sqrt(kvar),0.20050628841123108)
returns=.01*np.array([1.2,-1.0,.7,-2.2,1.8,-1.5,.4,-.9,2.1,-.6])
rv=252/len(returns)*np.sum(returns**2)
assert np.isclose(np.sum(returns**2),0.0019)
assert np.isclose(rv,0.04788)
assert np.isclose(1e6*(rv-kvar),7677.228307552221)
for ST in [3500.0,5000.0,6500.0]:
    left=-np.log(ST/F)
    right=-(ST-F)/F+quad(lambda K:max(K-ST,0)/K**2,1e-8,F,points=[min(ST,F)])[0]+quad(lambda K:max(ST-K,0)/K**2,F,np.inf,points=None)[0]
    assert abs(left-right)<1e-8
for h,target in [(200,0.043242889083533693),(100,0.04081101380712058),(50,0.04020277169244778),(25,0.04005069406115926)]:
    grid=np.arange(3000,7000+h/2,h);quotes=np.array([black(k,put=k<F) for k in grid])
    got=2*np.exp(r*T)/T*np.sum(h*quotes/grid**2)
    assert np.isclose(got,target)
T1,T2,T30=23/365,37/365,30/365
w30=(T1*.22**2*(T2-T30)+T2*.19**2*(T30-T1))/(T2-T1)
assert np.isclose(w30,0.0033546575342465754)
assert np.isclose(100*np.sqrt(w30/T30),20.20272258879976)
