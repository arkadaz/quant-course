import numpy as np
from scipy.stats import norm
S,K,r,sig,T=100.0,105.0,0.04,0.20,0.25
def call(x):
 d1=(np.log(x/K)+(r+0.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
 return x*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
d1=(np.log(S/K)+(r+0.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
delta=norm.cdf(d1);gamma=norm.pdf(d1)/(S*sig*np.sqrt(T));vega=S*norm.pdf(d1)*np.sqrt(T)
theta=-S*norm.pdf(d1)*sig/(2*np.sqrt(T))-r*K*np.exp(-r*T)*norm.cdf(d2);rho=K*T*np.exp(-r*T)*norm.cdf(d2)
assert np.isclose(norm.pdf(d1),0.37680506505494295)
assert np.isclose(delta,0.36771865542601334)
assert np.isclose(gamma,0.037680506505494295)
assert np.isclose(vega,18.840253252747147)
assert np.isclose(theta,-8.911340846318136)
assert np.isclose(rho,8.595247145971173)
assert np.isclose(0.01*vega,0.18840253252747147)
assert np.isclose(theta/365,-0.024414632455666124)
assert np.isclose(1e-4*rho,0.0008595247145971174)
exact=call(101)-call(100);approx=delta+0.5*gamma
assert np.isclose(exact,0.3866930136625868)
assert np.isclose(approx,0.3865589086787605)
assert np.isclose(exact-approx,0.0001341049838263222)
