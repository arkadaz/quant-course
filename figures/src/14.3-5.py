
from scipy.stats import norm
S=np.linspace(65,150,320);K=105.;r=.04;sig=.2;T=.25
d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T);rho=1e-4*K*T*np.exp(-r*T)*norm.cdf(d2)
ax.plot(S,rho,color=GOOD);ax.set_xlabel('Spot (USD)');ax.set_ylabel('Rho (USD per bp)')
