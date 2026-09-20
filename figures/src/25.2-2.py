rng=np.random.default_rng(11)
n,w,a,b,nu=120_000,3.1e-6,.07,.90,8
z=rng.standard_t(nu,n)/np.sqrt(nu/(nu-2))
h=np.empty(n);h[0]=w/(1-a-b);r=np.empty(n)
for t in range(n):
    if t: h[t]=w+a*r[t-1]**2+b*h[t-1]
    r[t]=np.sqrt(h[t])*z[t]
def acf(v,k):
    v=v-v.mean();return float((v[:-k]*v[k:]).mean()/v.var())
lags=np.arange(1,61)
ar=[acf(r,k) for k in lags]
aa=[acf(abs(r),k) for k in lags]
ax.bar(lags-0.2,ar,width=.4,color=MUTED,label='ACF of the return itself')
ax.bar(lags+0.2,aa,width=.4,color=ACCENT,label='ACF of the size of the return')
band=2/np.sqrt(n)
ax.axhspan(-band,band,color=GRID,alpha=.7,zorder=0)
ax.axhline(0,color=INK,lw=.8)
ax.annotate('95% band for pure noise',xy=(45,band),xytext=(0,8),textcoords='offset points',fontsize=7,color=MUTED)
ax.annotate('still 0.073 at 20 days',xy=(20,acf(abs(r),20)),xytext=(24,0.10),fontsize=7.5,color=ACCENT,
            arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.8))
ax.set_xlabel('lag (trading days)');ax.set_ylabel('autocorrelation')
ax.set_title('Direction has no memory; size has a memory that lasts months',loc='left')
ax.legend(fontsize=7,loc='upper right')
