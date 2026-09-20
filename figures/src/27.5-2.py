rng=np.random.default_rng(37)
n,T=600,251
B=np.zeros((n,3)); B[:,0]=1
B[:,1]=rng.normal(0,1,n).round(2)
B[:,2]=(rng.random(n)<0.18).astype(float)
se=rng.uniform(0.012,0.030,n)
r=B@np.array([0.0040,-0.0025,0.0060])+rng.standard_normal(n)*se
W=np.diag(1/se**2)
fit=lambda x:np.linalg.solve(B.T@W@B,B.T@W@x)
base=fit(r)
hist=rng.standard_normal((n,T))*se[:,None]
s=np.median(np.abs(np.log1p(hist)),axis=1)[7]
def resid(shock,d):
    cap=np.expm1(np.sign(shock)*d*s)
    v=shock if abs(np.log1p(shock))<=d*s else cap
    x=r.copy(); x[7]=v
    return abs((fit(x)-base)[1])*1e4
ds=np.linspace(2,40,160)
ax.semilogy(ds,[resid(3.40,d) for d in ds],color=BAD,lw=2.4,label='bad price: error you want gone')
ax.semilogy(ds,[resid(-0.18,d) for d in ds],color=GOOD,lw=2.4,label='real news: truth you want kept')
ax.axvspan(5,10,color=GRID,alpha=.9,zorder=0)
ax.annotate('what people use',xy=(7.5,0.55),ha='center',fontsize=8,color=MUTED)
ax.annotate('still 6.5 bp of pure error at 10',xy=(10,6.55),xytext=(13,2.3),fontsize=8,color=BAD,
            arrowprops=dict(arrowstyle='->',color=BAD,lw=.9))
ax.annotate('the real 9.3 bp only\nsurvives past about 24',xy=(24,9.27),xytext=(19,21),fontsize=8,color=GOOD,
            arrowprops=dict(arrowstyle='->',color=GOOD,lw=.9))
ax.set_xlabel('winsorization threshold on the robust score')
ax.set_ylabel('momentum factor moved, basis points (log scale)')
ax.set_title('No single threshold is right for both kinds of outlier',loc='left')
ax.legend(frameon=False,fontsize=8,loc='lower right')
