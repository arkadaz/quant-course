rng=np.random.default_rng(178);pdim=20;nobs=60
true=.0001*np.eye(pdim)+.00005*np.ones((pdim,pdim))
x=rng.multivariate_normal(np.zeros(pdim),true,nobs)
S=x.T@x/nobs;F=np.trace(S)/pdim*np.eye(pdim)
beta=sum(np.sum((np.outer(row,row)-S)**2) for row in x)/nobs**2
den=np.sum((S-F)**2);delta=min(1.,beta/den) if den>0 else 1.
test=rng.multivariate_normal(np.full(pdim,.0003),true,2520);ds=np.linspace(0,1,31);out=[]
for a in ds:
 u=np.linalg.solve((1-a)*S+a*F,np.ones(pdim));w=u/u.sum();r=test@w;out.append(np.sqrt(252)*r.mean()/r.std(ddof=1))
ax.plot(ds,out);ax.axvline(delta,color=WARM,ls='--',label='Training-only intensity');ax.set_xlabel('Shrinkage intensity');ax.set_ylabel('Synthetic test Sharpe (annualized)');ax.legend(fontsize=7)
