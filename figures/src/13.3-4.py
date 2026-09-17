
from scipy.stats import norm
S=np.linspace(65,150,320);K=105.;r=.04;sig=.2;T=.25
d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T)
th=(-S*norm.pdf(d1)*sig/(2*np.sqrt(T))-r*K*np.exp(-r*T)*norm.cdf(d2))/365
ax.plot(S,th,color=BAD);ax.axhline(0,color=INK,lw=1);ax.set_xlabel('Spot (USD)');ax.set_ylabel('Theta (USD per calendar day)')
