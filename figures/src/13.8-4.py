
from scipy.stats import norm
F=5000.;T=30/365;r=.04;s=.20;D=np.exp(-r*T);hs=np.array([200,100,50,25]);out=[]
for h in hs:
    k=np.arange(3000,7000+h/2,h);d1=(np.log(F/k)+.5*s*s*T)/(s*np.sqrt(T));d2=d1-s*np.sqrt(T)
    c=D*(F*norm.cdf(d1)-k*norm.cdf(d2));p=c-D*(F-k);q=np.where(k<F,p,c)
    out.append(100*np.sqrt(2/T*np.exp(r*T)*np.sum(h*q/k**2)))
ax.plot(hs,out,'o-',color=ACCENT);ax.axhline(20,color=GOOD,ls='--',label='Flat-vol input')
ax.set_xlabel('Strike spacing (SPX points)');ax.set_ylabel('Recovered fair volatility (%)');ax.invert_xaxis();ax.legend()
