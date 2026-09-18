x=np.linspace(-22,24,900);sd=6.0
y=stats.norm.pdf(x,0,sd)
ax.plot(x,y,color=ACCENT,lw=1.8)
ax.fill_between(x,0,y,where=x>=13.958,color=BAD,alpha=.35,label='worst 1% of days')
for v,c,ls,t in ((9.869,WARM,'--','VaR 95% 9.87'),(12.376,WARM,':','ES 95% 12.38'),(13.958,BAD,'--','VaR 99% 13.96'),(15.993,BAD,':','ES 99% 15.99')):
    ax.axvline(v,color=c,ls=ls,lw=1.3,label=t)
ax.set_xlabel('One-day loss on 500M USD, sigma 1.2% (USD million)');ax.set_ylabel('Probability per USD million')
ax.set_title('VaR marks the door; ES is the average room behind it',loc='left');ax.legend(fontsize=7,loc='upper left');ax.grid(alpha=.2)
