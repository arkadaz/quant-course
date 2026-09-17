rng=np.random.default_rng(176);rs=rng.normal(.007,.035,(12,36))
for i,r in enumerate(rs):
 w=np.r_[1,np.cumprod(1+r)];dd=np.max(1-w/np.maximum.accumulate(w));cg=w[-1]**(1/3)-1;sh=np.sqrt(12)*r.mean()/r.std(ddof=1);ax.scatter(sh,cg/dd,s=25);ax.annotate(str(i+1),(sh,cg/dd),xytext=(3,3),textcoords='offset points',fontsize=7)
ax.set_xlabel('Annualized Sharpe (cash = 0)');ax.set_ylabel('Three-year Calmar')
