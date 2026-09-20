
from scipy.stats import norm
F=5000.;T=30/365;r=.04;s=.20;D=np.exp(-r*T);k=np.arange(3000,7001,50)
d1=(np.log(F/k)+.5*s*s*T)/(s*np.sqrt(T));d2=d1-s*np.sqrt(T)
c=D*(F*norm.cdf(d1)-k*norm.cdf(d2));p=c-D*(F-k);q=np.where(k<5000,p,c)
contrib=2/T*np.exp(r*T)*50*q/k**2
ax.bar(k,contrib,width=42,color=np.where(k<5000,WARM,ACCENT))
ax.set_xlabel('Strike (SPX points)');ax.set_ylabel('Contribution to annual variance')
