
from scipy.stats import norm
S=5000.;K=5000.;r=.04;q=.015;T=.5;v=np.linspace(.05,.70,260);D=np.exp(-r*T)
d1=(np.log(S/K)+(r-q+.5*v*v)*T)/(v*np.sqrt(T));d2=d1-v*np.sqrt(T)
c=S*np.exp(-q*T)*norm.cdf(d1)-K*D*norm.cdf(d2);p=K*D*norm.cdf(-d2)-S*np.exp(-q*T)*norm.cdf(-d1)
ax.plot(100*v,c,label='Call',color=ACCENT);ax.plot(100*v,p,label='Put',color=WARM);ax.plot(100*v,c-p,'--',label='Call minus put',color=GOOD)
ax.set_xlabel('Volatility (% per sqrt year)');ax.set_ylabel('Price (SPX points)');ax.legend()
