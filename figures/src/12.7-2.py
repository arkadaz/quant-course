from scipy.stats import norm
sig=np.linspace(.12,.36,350);d1=(.02+.5*sig**2)/sig;d2=d1-sig;C=100*norm.cdf(d1)-100*np.exp(-.02)*norm.cdf(d2);loss=.5*(C-10.45)**2
ax.plot(sig*100,loss,color=ACCENT,lw=2);ax.scatter([30],[.5*(12.821581-10.45)**2],color=BAD,s=45,label='start');ax.scatter([23.9236],[0],color=GOOD,s=45,label='root');ax.set_xlabel('Annual volatility (%)');ax.set_ylabel('Half squared price error');ax.legend();ax.set_title('Root finding becomes a one-valley optimisation',loc='left')
