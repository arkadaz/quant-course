T=251
fac_vol=np.array([40_000.,70_000.,50_000.]);idio_vol=120_000.
C=np.array([[1,.25,.45],[.25,1,-.15],[.45,-.15,1]])
rng=np.random.default_rng(153)
fp=(np.linalg.cholesky(C)@rng.standard_normal((3,T)))*fac_vol[:,None]
fp[1]+=0.8/np.sqrt(251)*70_000
ip=rng.standard_normal(T)*idio_vol+1.6/np.sqrt(251)*idio_vol
trade=-rng.gamma(2.0,1500.,T)
ann=lambda x: x.mean()/x.std()*np.sqrt(251)
a=ann(ip); b=ann(fp.sum(axis=0)+ip); c=ann(fp.sum(axis=0)+ip+trade)
steps=[('idiosyncratic\nalone',a,GOOD),('after adding\nfactor PnL',b,WARM),('after adding\ntrading costs',c,BAD)]
for i,(lab,val,col) in enumerate(steps):
    ax.bar(i,val,color=col,width=.55)
    ax.annotate(f'{val:.3f}',xy=(i,val),xytext=(0,6),textcoords='offset points',fontsize=10,ha='center')
ax.annotate(f'-{a-b:.3f}',xy=(0.5,(a+b)/2),xytext=(0,0),textcoords='offset points',
            fontsize=9,ha='center',color=WARM)
ax.annotate(f'-{b-c:.3f}',xy=(1.5,(b+c)/2),xytext=(0,0),textcoords='offset points',
            fontsize=9,ha='center',color=BAD)
ax.annotate('',xy=(1,b),xytext=(0,a),arrowprops=dict(arrowstyle='->',color=WARM,lw=1.4))
ax.annotate('',xy=(2,c),xytext=(1,b),arrowprops=dict(arrowstyle='->',color=BAD,lw=1.4))
ax.annotate('costs add no risk at all,\nso they cut Sharpe one for one',xy=(2,c),xytext=(1.05,0.55),
            fontsize=8,color=BAD,arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.set_xticks(range(3));ax.set_xticklabels([s[0] for s in steps],fontsize=8)
ax.set_ylabel('Sharpe Ratio of the book, per year')
ax.set_ylim(0,2.05)
ax.set_title('Where the Sharpe Ratio goes',loc='left')
