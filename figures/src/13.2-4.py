
from scipy.stats import norm
S=100.;K=105.;r=.04;T=.25;v=np.linspace(.005,1.2,320)
d1=(np.log(S/K)+(r+.5*v**2)*T)/(v*np.sqrt(T));d2=d1-v*np.sqrt(T);c=S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
ax.plot(100*v,c,color=ACCENT);ax.axhline(S,color=MUTED,ls='--',label='Upper bound S0')
ax.set_xlabel('Volatility (% per sqrt year)');ax.set_ylabel('Call value (USD)');ax.legend()
