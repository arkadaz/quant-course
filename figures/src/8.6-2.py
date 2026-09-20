x=np.linspace(-8,8,320);mean=0.04;sd=2.0
fx=stats.norm.pdf(x,loc=mean,scale=sd)
ax.plot(x,fx,color=ACCENT,lw=2)
ax.axvline(mean,color=BAD,ls='--',label='mean = 0.04%')
ax.fill_between(x,0,fx,where=(x>=mean-sd)&(x<=mean+sd),color=GOOD,alpha=0.25,label='mean +/- 1 SD')
ax.set_xlabel('SPX return (%)');ax.set_ylabel('density');ax.legend(loc='upper left')
ax.set_title('The SPX marginal keeps mean 0.04% and SD 2%',fontsize=9,loc='left')
