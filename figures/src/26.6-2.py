T=251
fac_vol=np.array([40_000.,70_000.,50_000.]);idio_vol=120_000.
C=np.array([[1,.25,.45],[.25,1,-.15],[.45,-.15,1]])
rng=np.random.default_rng(153)
fp=(np.linalg.cholesky(C)@rng.standard_normal((3,T)))*fac_vol[:,None]
fp[1]+=0.8/np.sqrt(251)*70_000
ip=rng.standard_normal(T)*idio_vol+1.6/np.sqrt(251)*idio_vol
trade=-rng.gamma(2.0,1500.,T)
labs=['market','style','industry','idio','trading']
usd=[fp[0].sum(),fp[1].sum(),fp[2].sum(),ip.sum(),trade.sum()]
ann=lambda x: x.mean()/x.std()*np.sqrt(251)
sr=[ann(fp[0]),ann(fp[1]),ann(fp[2]),ann(ip),np.nan]
cols=[BAD if u<0 else (GOOD if u>2e6 else WARM) for u in usd]
fig=ax.figure;fig.delaxes(ax)
a1=fig.add_subplot(1,2,1)
a1.barh(range(5),np.array(usd)/1e6,color=cols,height=.6)
for i,u in enumerate(usd):
    a1.annotate(f'{u/1e6:+.2f}M',xy=(u/1e6,i),xytext=(6 if u>0 else -6,-3),
                textcoords='offset points',fontsize=8,ha='left' if u>0 else 'right')
a1.axvline(0,color=INK,lw=.9)
a1.set_yticks(range(5));a1.set_yticklabels(labs)
a1.set_xlabel('PnL for the year (USD million)');a1.set_xlim(-1.6,4.7)
a1.set_title('In dollars',loc='left',fontsize=9)
a2=fig.add_subplot(1,2,2)
a2.barh(range(4),sr[:4],color=cols[:4],height=.6)
for i,s in enumerate(sr[:4]):
    a2.annotate(f'{s:+.2f}',xy=(s,i),xytext=(6 if s>0 else -6,-3),textcoords='offset points',
                fontsize=8,ha='left' if s>0 else 'right')
a2.axvline(0,color=INK,lw=.9)
a2.set_yticks(range(4));a2.set_yticklabels(labs[:4])
a2.set_xlabel('PnL divided by the risk it used (per year)');a2.set_xlim(-0.9,2.4)
a2.set_title('Per unit of risk spent',loc='left',fontsize=9)
