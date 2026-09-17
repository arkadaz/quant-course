
from scipy.stats import norm
S=np.linspace(75,130,260);K=105.;r=.04;sig=.2;t=.25
d1=(np.log(S/K)+(r+.5*sig**2)*t)/(sig*np.sqrt(t));d2=d1-sig*np.sqrt(t)
call=S*norm.cdf(d1)-K*np.exp(-r*t)*norm.cdf(d2)
S0=100.;c0=2.39087696;delta=.367718655;tangent=c0+delta*(S-S0)
ax.plot(S,call,label='Call value',color=ACCENT);ax.plot(S,tangent,'--',label='Delta tangent',color=WARM)
ax.axvline(S0,color=MUTED,lw=1);ax.set_xlabel('Spot (USD)');ax.set_ylabel('Value (USD)');ax.legend()
