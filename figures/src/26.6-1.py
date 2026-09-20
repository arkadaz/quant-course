T=251
fac_vol=np.array([40_000.,70_000.,50_000.]);idio_vol=120_000.
C=np.array([[1,.25,.45],[.25,1,-.15],[.45,-.15,1]])
rng=np.random.default_rng(153)
fp=(np.linalg.cholesky(C)@rng.standard_normal((3,T)))*fac_vol[:,None]
fp[1]+=0.8/np.sqrt(251)*70_000
ip=rng.standard_normal(T)*idio_vol+1.6/np.sqrt(251)*idio_vol
trade=-rng.gamma(2.0,1500.,T)
d=np.arange(1,T+1)
ax.plot(d,np.cumsum(fp.sum(axis=0)+ip+trade)/1e6,color=INK,lw=2.8,label='the book, as the accounts show it')
ax.plot(d,np.cumsum(ip)/1e6,color=GOOD,lw=2.0,label='idiosyncratic: picking stocks')
ax.plot(d,np.cumsum(fp.sum(axis=0))/1e6,color=WARM,lw=2.0,label='factor: exposures')
ax.plot(d,np.cumsum(trade)/1e6,color=BAD,lw=2.0,label='trading: costs')
ax.axhline(0,color=GRID,lw=1.2)
for y,lab,col in ((3.582,'+3.58M',GOOD),(0.670,'+0.67M',WARM),(-0.753,'-0.75M',BAD),(3.500,'+3.50M',INK)):
    ax.annotate(lab,xy=(T,y),xytext=(6,-3),textcoords='offset points',fontsize=8,color=col)
ax.annotate('the only line whose direction\nyou can predict in advance',xy=(150,-0.45),
            xytext=(58,-1.55),fontsize=8,color=BAD,arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.set_xlabel('trading day of the year');ax.set_ylabel('cumulative PnL (USD million)')
ax.set_xlim(0,T+26)
ax.set_title('One book, three stories running at once',loc='left')
ax.legend(fontsize=7,loc='upper left')
