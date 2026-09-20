rng=np.random.default_rng(11)
T,rho,s=251,0.12,0.01
def newey(x,lags):
    t=len(x);c=lambda l:(x[l:]@x[:t-l])/t
    v=c(0)
    for l in range(1,lags+1): v+=2*(1-l/(1+lags))*c(l)
    return v
truev=s*s/(1-rho)**2
lags=np.arange(0,16)
got=np.zeros(len(lags))
for _ in range(400):
    e=rng.standard_normal(T+200);x=np.zeros(T+200)
    for t in range(1,T+200): x[t]=rho*x[t-1]+s*e[t]
    x=x[200:]
    for i,l in enumerate(lags): got[i]+=newey(x,l)/truev
got/=400
ax.plot(lags,got*100,color=ACCENT,lw=2.4,marker='o',ms=5)
ax.axhline(100,color=BAD,ls='--',lw=1.8)
ax.annotate('the long-run variance you actually want',xy=(9,100),xytext=(0,6),
            textcoords='offset points',fontsize=8,color=BAD)
for l,lab in ((0,'no correction'),(5,'five lags')):
    ax.plot(l,got[l]*100,'o',color=INK,ms=8)
    ax.annotate(f'{lab}: {got[l]*100:.1f}%',xy=(l,got[l]*100),xytext=(10,-12),
                textcoords='offset points',fontsize=8)
ax.set_xlabel('lags included in the Newey-West sum');ax.set_ylabel('% of the long-run variance captured')
ax.set_ylim(72,104)
ax.set_title('Autocorrelation of 0.12 hides a fifth of the risk',loc='left')
