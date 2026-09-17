from scipy.stats import norm
sig=np.linspace(.03,.65,400);S=K=100;r=.02;T=1;d1=(np.log(S/K)+(r+.5*sig**2)*T)/(sig*np.sqrt(T));d2=d1-sig*np.sqrt(T);C=S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
ax.plot(sig*100,C,color=ACCENT,lw=2);ax.axhline(10.45,color=WARM,ls='--',label='market USD 10.45');ax.scatter([23.9236],[10.45],color=GOOD,s=48);ax.set_xlabel('Annual volatility (%)');ax.set_ylabel('Call price (USD/share)');ax.legend();ax.set_title('Implied volatility is a price-curve crossing',loc='left')
