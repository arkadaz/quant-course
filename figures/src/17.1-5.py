c=np.linspace(.90,.999,300);z=stats.norm.ppf(c);ratio=stats.norm.pdf(z)/((1-c)*z)
ax.plot(100*c,ratio,color=ACCENT,lw=2);ax.scatter([95,99],[stats.norm.pdf(stats.norm.ppf(.95))/.05/stats.norm.ppf(.95),stats.norm.pdf(stats.norm.ppf(.99))/.01/stats.norm.ppf(.99)],color=BAD);ax.set_xlabel('Confidence level (%)');ax.set_ylabel('ES / VaR under normal model');ax.grid(alpha=.25)
