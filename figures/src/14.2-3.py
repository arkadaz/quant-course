
from scipy.stats import norm
S=np.linspace(70,140,260);K=105.;r=.04;sig=.2;T=.25
d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
ax.plot(S,norm.cdf(d1),label='Phi(d1): share-weighted',color=ACCENT);ax.plot(S,norm.cdf(d2),label='Phi(d2): exercise probability',color=WARM)
ax.set_xlabel('Spot (USD)');ax.set_ylabel('Quantity');ax.set_ylim(0,1);ax.legend()
