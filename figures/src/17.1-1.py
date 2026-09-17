x=np.linspace(-500,900,700);m=-4;s=220;v=stats.norm.ppf(.99,m,s);e=m+s*stats.norm.pdf(stats.norm.ppf(.99))/.01
ax.plot(x,stats.norm.pdf(x,m,s));ax.fill_between(x,0,stats.norm.pdf(x,m,s),where=x>=v,color=BAD,alpha=.3)
ax.axvline(v,color=WARM,label='VaR 99%');ax.axvline(e,color=BAD,label='ES 99%');ax.set_xlabel('One-day loss (USD thousand)');ax.set_ylabel('Density per USD thousand');ax.legend()
