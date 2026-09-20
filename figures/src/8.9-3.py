rng=np.random.default_rng(0)
S=np.array([[0.0004,0.00024],[0.00024,0.0009]]);L=np.linalg.cholesky(S)
ns=np.array([50,100,250,800,2500,8000,25000]);z=rng.normal(size=(ns[-1],2));r=z@L.T
errs=[np.cov(r[:n],rowvar=False,ddof=1)[0,1]*10000 for n in ns];target=S[0,1]*10000
ax.semilogx(ns,errs,marker='o',color=ACCENT,lw=2,label='sample covariance')
ax.axhline(target,color=BAD,ls='--',label='target = 2.40')
ax.set_xlabel('scenario count n');ax.set_ylabel(r'Covariance $((\text{percentage points})^2/\text{day})$')
ax.legend(loc='upper right',fontsize=8);ax.set_title('Sample covariance approaches the target',fontsize=9,loc='left')
