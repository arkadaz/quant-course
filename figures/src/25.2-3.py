rng=np.random.default_rng(11)
n,w,a,b,nu=400_000,3.1e-6,.07,.90,8
z=rng.standard_t(nu,n)/np.sqrt(nu/(nu-2))
h=np.empty(n);h[0]=w/(1-a-b);r=np.empty(n)
for t in range(n):
    if t: h[t]=w+a*r[t-1]**2+b*h[t-1]
    r[t]=np.sqrt(h[t])*z[t]
ms=np.array([1,5,21,63,126])
K=[stats.kurtosis(r[:n//m*m].reshape(-1,m).sum(axis=1),fisher=False) for m in ms]
ax.semilogx(ms,K,color=ACCENT,lw=2.2,marker='o',ms=7)
ax.axhline(3.0,color=BAD,ls='--',lw=1.6)
ax.annotate('Normal sits at 3',xy=(80,3.0),xytext=(0,7),textcoords='offset points',fontsize=8,color=BAD)
names=['1 day','1 week','1 month','1 quarter','6 months']
for m,k,nm in zip(ms,K,names):
    ax.annotate(f'{k:.2f}\n{nm}',xy=(m,k),xytext=(0,10),textcoords='offset points',fontsize=7.5,ha='center')
ax.set_xticks(ms);ax.set_xticklabels([str(m) for m in ms])
ax.set_xlabel('trading days summed into one observation');ax.set_ylabel('kurtosis')
ax.set_ylim(2.6,7.1)
ax.set_title('The same data: fat tails daily, nearly Normal over six months',loc='left')
