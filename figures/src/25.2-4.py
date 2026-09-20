rng=np.random.default_rng(11)
n,w,a,b,nu=120_000,3.1e-6,.07,.90,8
z=rng.standard_t(nu,n)/np.sqrt(nu/(nu-2))
h=np.empty(n);h[0]=w/(1-a-b);r=np.empty(n)
for t in range(n):
    if t: h[t]=w+a*r[t-1]**2+b*h[t-1]
    r[t]=np.sqrt(h[t])*z[t]
for series,col,lab,mk in ((r,ACCENT,'daily returns','o'),
                          (r[:n//21*21].reshape(-1,21).sum(axis=1),GOOD,'monthly returns (21 days)','s')):
    s=np.sort(series)/series.std()
    q=stats.norm.ppf((np.arange(1,len(s)+1)-.5)/len(s))
    step=max(1,len(s)//2500)
    ax.plot(q[::step],s[::step],mk,color=col,ms=2.2,label=lab,alpha=.75)
lim=7
ax.plot([-lim,lim],[-lim,lim],color=BAD,lw=1.6,ls='--',label='where Normal data would sit')
ax.set_xlim(-5,5);ax.set_ylim(-12,12)
ax.annotate('tails bend away from the line',xy=(-4.2,-9),xytext=(-4.6,-6.0),fontsize=7.5,color=ACCENT,
            arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.8))
ax.set_xlabel('Normal quantile');ax.set_ylabel('observed quantile (in units of sigma)')
ax.set_title('QQ plot: daily returns bend at the tails, monthly returns much less',loc='left')
ax.legend(fontsize=7,loc='upper left')
