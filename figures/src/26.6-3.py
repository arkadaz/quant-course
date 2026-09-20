T=251
fac_vol=np.array([40_000.,70_000.,50_000.]);idio_vol=120_000.
C=np.array([[1,.25,.45],[.25,1,-.15],[.45,-.15,1]])
rng=np.random.default_rng(153)
fp=(np.linalg.cholesky(C)@rng.standard_normal((3,T)))*fac_vol[:,None]
fp[1]+=0.8/np.sqrt(251)*70_000
ip=rng.standard_normal(T)*idio_vol+1.6/np.sqrt(251)*idio_vol
mf=fp.sum(axis=0)[:240].reshape(12,20).sum(axis=1)/1e6
mi=ip[:240].reshape(12,20).sum(axis=1)/1e6
x=np.arange(12)
ax.bar(x-0.19,mf,width=.36,color=WARM,label='factor')
ax.bar(x+0.19,mi,width=.36,color=GOOD,label='idiosyncratic')
dis=np.sign(mf)!=np.sign(mi)
for i in np.where(dis)[0]:
    ax.annotate('',xy=(i,max(mf[i],mi[i])+0.12),xytext=(i,max(mf[i],mi[i])+0.02),
                arrowprops=dict(arrowstyle='-',color=INK,lw=1.4))
    ax.annotate('x',xy=(i,max(mf[i],mi[i])+0.13),fontsize=8,color=INK,ha='center')
ax.axhline(0,color=INK,lw=.9)
ax.annotate('x marks a month where the two disagree: 5 of 12',xy=(5.5,1.22),fontsize=8,color=INK,ha='center')
ax.set_xticks(x);ax.set_xticklabels([f'M{i+1}' for i in range(12)],fontsize=7.5)
ax.set_ylabel('PnL for the month (USD million)')
ax.set_ylim(-1.0,1.45)
ax.set_title('A bad month tells you nothing until you split it',loc='left')
ax.legend(fontsize=7,loc='lower left')
