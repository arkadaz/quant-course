
from scipy.stats import norm
S=np.linspace(65,135,320);K=100.;sig=.2;rem=.25
d1=(np.log(S/K)+.5*sig**2*rem)/(sig*np.sqrt(rem));d2=d1-sig*np.sqrt(rem);back=S*norm.cdf(d1)-K*norm.cdf(d2);front=np.maximum(S-K,0)
ax.plot(S,back,label='Back call value',color=ACCENT);ax.plot(S,front,label='Expired front payoff',color=WARM);ax.fill_between(S,front,back,color=GOOD,alpha=.18,label='Calendar value')
ax.set_xlabel('Spot at front expiry (USD)');ax.set_ylabel('Value (USD per share)');ax.legend()
