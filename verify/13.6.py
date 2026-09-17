import numpy as np
from scipy.stats import norm
S,r,sig,T1,T2=100.0,0.0,0.20,0.25,0.50
def call(K,T):
 d1=(np.log(S/K)+(r+0.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
 return S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
def put(K,T): return call(K,T)-S+K*np.exp(-r*T)
def gamma(K,T):
 d1=(np.log(S/K)+(r+0.5*sig**2)*T)/(sig*np.sqrt(T));return norm.pdf(d1)/(S*sig*np.sqrt(T))
def vega_pt(K,T):
 d1=(np.log(S/K)+(r+0.5*sig**2)*T)/(sig*np.sqrt(T));return .01*S*norm.pdf(d1)*np.sqrt(T)
prem=np.array([call(100,T1)+put(100,T1),put(90,T1)+call(110,T1),call(110,T1)-put(90,T1),call(90,T1)-2*call(100,T1)+call(110,T1),call(100,T2)-call(100,T1)])
expected=np.array([7.975522335348984,1.6663282879308916,.24156649578355527,3.6908059525819077,1.6494366120271735])
assert np.allclose(prem,expected)
vegas=np.array([2*vega_pt(100,T1),vega_pt(90,T1)+vega_pt(110,T1),vega_pt(110,T1)-vega_pt(90,T1),vega_pt(90,T1)-2*vega_pt(100,T1)+vega_pt(110,T1),vega_pt(100,T2)-vega_pt(100,T1)])
assert np.allclose(vegas,[.39844391409476404,.24116537410807062,.02417682675684615,-.15727853998669336,.0821684785591228])
assert np.isclose(100-prem[0],92.02447766465102)
assert np.isclose(100+prem[0],107.97552233534898)
var04=.25*.2**2+.25*.3**2+2*.5*.5*.2*.3*.4;var02=.25*.2**2+.25*.3**2+2*.5*.5*.2*.3*.2
assert np.isclose(var04,.0445) and np.isclose(var02,.0385)
assert np.isclose(1e6*(var04-var02),6000.0)
