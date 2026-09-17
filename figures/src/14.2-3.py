z=np.linspace(-5,5,600); n=30; df=5; scale=np.sqrt((df-2)/df); approx=stats.t.pdf(z*np.sqrt(n)/scale,df)*np.sqrt(n)/scale; normal=stats.norm.pdf(z)
ax.plot(z,approx,color=SERIES[0],lw=2,label='scaled t mean proxy'); ax.plot(z,normal,color=BAD,lw=1.5,ls='--',label='standard normal'); ax.set(xlabel='Standardized outcome',ylabel='Density',ylim=(0,.46)); ax.legend(fontsize=7); ax.grid(alpha=.25)
