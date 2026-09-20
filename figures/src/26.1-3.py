n=np.arange(50,3001)
m=60;T=251
emp=n*(n+1)/2
fac=m*(m+1)/2+n
ax.loglog(n,emp,color=BAD,lw=2.3,label='covariance estimated directly: n(n+1)/2')
ax.loglog(n,fac,color=ACCENT,lw=2.3,label='factor model: 1,830 + n')
ax.axhline(T,color=MUTED,ls='--',lw=1.5,label='independent observations you have: 251 days')
ax.axvline(251,color=GRID,lw=6,alpha=.8)
ax.annotate('beyond 251 stocks the direct route\nhas portfolios it scores at zero risk',
            xy=(251,4e3),xytext=(330,3.2e2),fontsize=7.5,color=MUTED,
            arrowprops=dict(arrowstyle='->',color=MUTED,lw=.9))
for x in (500,3000):
    ax.plot(x,x*(x+1)/2,'o',color=BAD,ms=6)
    ax.plot(x,m*(m+1)/2+x,'o',color=ACCENT,ms=6)
    ax.annotate(f'{int(x*(x+1)/2):,}',xy=(x,x*(x+1)/2),xytext=(-6,9),textcoords='offset points',
                fontsize=7.5,color=BAD,ha='right')
    ax.annotate(f'{int(m*(m+1)/2+x):,}',xy=(x,m*(m+1)/2+x),xytext=(-6,-14),textcoords='offset points',
                fontsize=7.5,color=ACCENT,ha='right')
ax.set_xlabel('number of stocks');ax.set_ylabel('numbers you must estimate')
ax.set_title('One route grows with the square of the universe; the other does not',loc='left')
ax.legend(fontsize=7,loc='upper left')
