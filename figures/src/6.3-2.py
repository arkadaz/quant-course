x=np.linspace(-10,8,400);sx,sy,rho,y0=2.5,3.0,0.6,-3.0
mean=rho*sx/sy*y0;sd=sx*np.sqrt(1-rho**2)
marg=stats.norm.pdf(x,0,sx);cond=stats.norm.pdf(x,mean,sd)
ax.plot(x,marg,color=MUTED,lw=2,label='AAPL marginal: mean 0%, sd 2.5%')
ax.plot(x,cond,color=BAD,lw=2,label='AAPL | MSFT=-3%: mean -1.5%, sd 2.0%')
ax.axvline(mean,color=BAD,ls='--',lw=0.8)
ax.set_xlabel('AAPL return (%)');ax.set_ylabel('density per percentage point')
ax.legend(loc='upper left');ax.set_title('Conditioning updates both location and uncertainty',fontsize=9,loc='left')
