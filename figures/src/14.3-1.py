
from scipy.stats import norm
S=np.linspace(70,140,300);K=105.;r=.04;sig=.2
for T,c in zip([1.0,.25,.05],[MUTED,ACCENT,WARM]):
 d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));ax.plot(S,norm.cdf(d1),color=c,label=f'{T:.2f}y')
ax.set_xlabel('Spot (USD)');ax.set_ylabel('Delta');ax.set_ylim(0,1);ax.legend(title='Time left')
