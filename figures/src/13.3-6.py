
from scipy.stats import norm
S0=100.;K=105.;r=.04;sig=.2;T=.25;c0=2.3908769614699386;d=.36771865542601334;g=.037680506505494295
h=np.linspace(-15,15,301);S=S0+h;d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T);c=S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2);chg=c-c0
ax.plot(h,d*h-chg,label='Delta error',color=WARM);ax.plot(h,d*h+.5*g*h*h-chg,label='Delta-gamma error',color=ACCENT);ax.axhline(0,color=INK,lw=1)
ax.set_xlabel('Spot shock (USD)');ax.set_ylabel('Approximation minus reprice (USD)');ax.legend()
