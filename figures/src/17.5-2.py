rng=np.random.default_rng(175)
z=rng.normal(size=(20000,12));dt=1/12
s=100*np.exp(np.cumsum((.03-.5*.2**2)*dt+.2*np.sqrt(dt)*z,axis=1))
x=np.exp(-.03)*np.maximum(s.mean(axis=1)-100,0)
y=np.exp(-.03)*s[:,-1]
n=np.array([100,500,2000,10000,20000]);xc=x-.5*(y-100)
ax.loglog(n,x.std(ddof=1)/np.sqrt(n),marker='o',label='Plain');ax.loglog(n,xc.std(ddof=1)/np.sqrt(n),marker='o',label='Control c=0.5');ax.set_xlabel('Independent paths');ax.set_ylabel('Estimated SE (USD)');ax.legend()
