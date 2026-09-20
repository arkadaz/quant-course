
from scipy.stats import norm
S=np.linspace(70,140,300);K=105.;r=.04;sig=.2
for T,c in zip([.05,.25,1.0],[WARM,ACCENT,MUTED]):
 d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));v=.01*S*norm.pdf(d1)*np.sqrt(T);ax.plot(S,v,color=c,label=f'{T:.2f}y')
ax.set_xlabel('Spot (USD)');ax.set_ylabel('Vega (USD per vol point)');ax.legend(title='Time left')
