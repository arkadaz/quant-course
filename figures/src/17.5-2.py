rng=np.random.default_rng(175)
z=rng.normal(size=(20000,12));dt=1/12
drift=(.02-.5*.3**2)*dt;shock=.3*np.sqrt(dt)
s=100*np.exp(np.cumsum(drift+shock*z,axis=1))
x=np.exp(-.02)*np.maximum(s.mean(axis=1)-100,0)
y=np.exp(-.02)*s[:,-1]
n=np.array([100,500,2000,10000,20000]);xc=x-.33*(y-100)
ax.loglog(n,x.std(ddof=1)/np.sqrt(n),marker='o',label='Plain');ax.loglog(n,xc.std(ddof=1)/np.sqrt(n),marker='o',label='Control c=0.33');ax.set_xlabel('Independent paths');ax.set_ylabel('Estimated SE (USD)');ax.legend()
