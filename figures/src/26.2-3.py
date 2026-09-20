n=np.logspace(2,5.2,300)
mu,sig=0.020,0.35
ax.loglog(n,np.sqrt(n)*mu/sig,color=BAD,lw=2.4,label='if alpha per stock stays at 2% a year')
ax.loglog(n,np.sqrt(n)*(mu*(500/n)**0.25)/sig,color=ACCENT,lw=2.4,ls='--',
          label='if alpha per stock fades as n to the -1/4')
ax.axhspan(0.8,2.5,color=GRID,alpha=.8,zorder=0)
ax.annotate('where real funds live',xy=(1.3e2,1.35),fontsize=8,color=MUTED)
for N in (8000,100000):
    ax.plot(N,np.sqrt(N)*mu/sig,'o',color=BAD,ms=6)
    ax.annotate(f'{np.sqrt(N)*mu/sig:.1f}',xy=(N,np.sqrt(N)*mu/sig),xytext=(-4,9),
                textcoords='offset points',fontsize=8,color=BAD,ha='right')
ax.annotate('a Sharpe of 18 means one losing year\nper age of the universe',
            xy=(1e5,18.07),xytext=(2.4e3,26),fontsize=8,color=BAD,
            arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.set_xlabel('stocks in the universe');ax.set_ylabel('Sharpe Ratio per year')
ax.set_title('One of the three assumptions has to give, and it is the alpha',loc='left')
ax.legend(fontsize=7,loc='lower right')
