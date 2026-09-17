rng=np.random.default_rng(642);m=60000;s=1/12;jan=rng.normal(0,np.sqrt(s),m);rest=rng.normal(0,np.sqrt(1-s),m);year=jan+rest;cov=np.cov(jan,year,ddof=0)[0,1];rho=np.corrcoef(jan,year)[0,1]
ix=np.arange(0,m,30);ax.scatter(jan[ix],year[ix],s=8,alpha=.22,color=ACCENT,edgecolors='none')
xx=np.linspace(jan[ix].min(),jan[ix].max(),100);ax.plot(xx,xx,color=GOOD,lw=2,label='conditional mean: year = January')
ax.set_xlabel('January cumulative result');ax.set_ylabel('Full-year cumulative result');ax.set_title(f'Monte Carlo: covariance={cov:.4f}, correlation={rho:.3f}',loc='left');ax.legend(loc='upper left')
