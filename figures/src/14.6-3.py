
from scipy.stats import norm
S=np.linspace(70,135,350);sig=.2;T1=.25;T2=.5
def g(K,T):
 d1=(np.log(S/K)+.5*sig**2*T)/(sig*np.sqrt(T));return norm.pdf(d1)/(S*sig*np.sqrt(T))
sets={'Straddle':2*g(100,T1),'Strangle':g(90,T1)+g(110,T1),'Risk reversal':g(110,T1)-g(90,T1),'Butterfly':g(90,T1)-2*g(100,T1)+g(110,T1),'Calendar':g(100,T2)-g(100,T1)}
for (name,y),c in zip(sets.items(),[ACCENT,WARM,BAD,GOOD,MUTED]): ax.plot(S,y,label=name,color=c)
ax.axhline(0,color=INK,lw=1);ax.set_xlabel('Spot (USD)');ax.set_ylabel('Gamma (per USD)');ax.legend(ncol=2)
