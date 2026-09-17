
from scipy.stats import norm
S=np.linspace(60,145,320);K=105.;r=.04;sig=.2;T=.25
d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
c=S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
ax.plot(S,np.maximum(S-K,0),'--',color=MUTED,label='Expiry payoff');ax.plot(S,c,color=ACCENT,label='Value with 0.25y left')
ax.set_xlabel('Spot (USD)');ax.set_ylabel('USD per share');ax.legend()
