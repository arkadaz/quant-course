rng=np.random.default_rng(3)
se,sn,P0,n=0.0256,0.012,50.0,400_000
m=P0+np.cumsum(se*rng.standard_normal(n))
p=m+sn*rng.standard_normal(n)
dp=np.diff(p)
lags=np.arange(1,13)
a=[float(np.mean(dp[k:]*dp[:-k])/dp.var()) for k in lags]
ax.bar(lags,a,width=.55,color=[BAD]+[MUTED]*11)
band=2/np.sqrt(n)
ax.axhspan(-band,band,color=GRID,alpha=.9,zorder=0)
ax.axhline(0,color=INK,lw=.9)
ax.annotate(f'lag 1 = {a[0]:.3f}\nthe model says exactly this',xy=(1,a[0]),xytext=(2.4,-0.115),fontsize=8,color=BAD,
            arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.annotate('everything else inside the noise band',xy=(7,band),xytext=(0,10),
            textcoords='offset points',fontsize=7.5,color=MUTED,ha='center')
ax.set_xticks(lags)
ax.set_xlabel('lag (minutes)');ax.set_ylabel('autocorrelation of the price change')
ax.set_title('One negative bar at lag 1, then silence: the signature of a spread',loc='left')
