
from scipy.stats import norm
S=np.linspace(70,140,300);K=105.;r=.04;sig=.2
for T,c in zip([1.0,.25,.05],[MUTED,ACCENT,WARM]):
 d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));g=norm.pdf(d1)/(S*sig*np.sqrt(T));ax.plot(S,g,color=c,label=f'{T:.2f}y')
ax.set_xlabel('Spot (USD)');ax.set_ylabel('Gamma (per USD)');ax.legend(title='Time left')
