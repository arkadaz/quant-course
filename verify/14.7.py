import numpy as np
from scipy.integrate import quad
S,K,r,q,T=100.0,100.0,.03,.01,1.0
kappa,theta,xi,rho,v0=2.0,.04,.30,-.70,.09
mean=theta+(v0-theta)*np.exp(-kappa*T);avg=theta+(v0-theta)*(1-np.exp(-kappa*T))/(kappa*T)
assert np.isclose(mean,.046766764161830635)
assert np.isclose(avg,.06161661791908468)
assert 2*kappa*theta>=xi**2
x=np.log(S)
def cf(u):
 b=kappa-rho*xi*1j*u;d=np.sqrt(b*b+xi*xi*(u*u+1j*u));g=(b-d)/(b+d)
 A=1j*u*(r-q)*T+kappa*theta/xi**2*((b-d)*T-2*np.log((1-g*np.exp(-d*T))/(1-g)))
 B=(b-d)/xi**2*(1-np.exp(-d*T))/(1-g*np.exp(-d*T))
 return np.exp(1j*u*x+A+B*v0)
phi_mi=cf(-1j)
f1=lambda u: np.real(np.exp(-1j*u*np.log(K))*cf(u-1j)/(1j*u*phi_mi))
f2=lambda u: np.real(np.exp(-1j*u*np.log(K))*cf(u)/(1j*u))
P1=.5+quad(f1,1e-9,150,limit=500,epsabs=1e-10)[0]/np.pi
P2=.5+quad(f2,1e-9,150,limit=500,epsabs=1e-10)[0]/np.pi
C=S*np.exp(-q*T)*P1-K*np.exp(-r*T)*P2
assert np.isclose(phi_mi,S*np.exp((r-q)*T))
assert np.isclose(P1,.6307063903355049)
assert np.isclose(P2,.5359218816665972)
assert np.isclose(C,10.434776050194316)
