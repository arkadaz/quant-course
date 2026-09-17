rng=np.random.default_rng(178);pdim=20;nobs=60
true=.0001*np.eye(pdim)+.00005*np.ones((pdim,pdim))
x=rng.multivariate_normal(np.zeros(pdim),true,nobs)
S=x.T@x/nobs;F=np.trace(S)/pdim*np.eye(pdim)
beta=sum(np.sum((np.outer(row,row)-S)**2) for row in x)/nobs**2
den=np.sum((S-F)**2);delta=min(1.,beta/den) if den>0 else 1.
e1=np.linalg.eigvalsh(S);e2=np.linalg.eigvalsh((1-delta)*S+delta*F);ax.plot(np.arange(1,21),e1*1e4,marker='.',label='Sample');ax.plot(np.arange(1,21),e2*1e4,marker='.',label=f'Shrunk, intensity={delta:.3f}');ax.set_xlabel('Eigenvalue rank');ax.set_ylabel('Daily eigenvalue (x 0.0001)');ax.legend(fontsize=7)
