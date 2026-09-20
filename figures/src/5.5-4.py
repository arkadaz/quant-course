rng=np.random.default_rng(0)
nmax=3200;x=rng.normal(2,1,nmax);y=rng.normal(3,1,nmax)
ns=np.array([50,200,800,3200])
errs=[abs(np.mean(x[:n]*y[:n])-np.mean(x[:n])*np.mean(y[:n])) for n in ns]
ax.plot(ns,errs,marker='o',color=GOOD,lw=2)
ax.set_xscale('log');ax.set_yscale('log');ax.set_xlabel('sample size');ax.set_ylabel('|sample E[XY] − sample E[X]E[Y]|')
ax.set_title('Product-factorization error tends toward zero, with noise',fontsize=9,loc='left')
