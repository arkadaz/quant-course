
from scipy.stats import norm
h=np.linspace(-8,8,201);S=100+h;K=105.;r=.04;sig=.2;t=.25
d1=(np.log(S/K)+(r+.5*sig**2)*t)/(sig*np.sqrt(t));d2=d1-sig*np.sqrt(t)
c=S*norm.cdf(d1)-K*np.exp(-r*t)*norm.cdf(d2);c0=2.39087696;delta=.367718655;gamma=.0376805065
ax.plot(h,c-(c0+delta*h),label='Exact convexity error',color=ACCENT);ax.plot(h,.5*gamma*h*h,'--',label=r'$0.5\,\Gamma h^2$',color=GOOD)
ax.set_xlabel('Spot move h (USD)');ax.set_ylabel('Error (USD per call)');ax.legend()
