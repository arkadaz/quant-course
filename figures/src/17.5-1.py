rng=np.random.default_rng(175)
z=rng.normal(size=(20000,12));dt=1/12
s=100*np.exp(np.cumsum((.03-.5*.2**2)*dt+.2*np.sqrt(dt)*z,axis=1))
x=np.exp(-.03)*np.maximum(s.mean(axis=1)-100,0)
y=np.exp(-.03)*s[:,-1]
for row in s[:12]:ax.plot(np.arange(13),np.r_[100,row],alpha=.65,lw=1)
ax.set_xlabel('Month');ax.set_ylabel('Simulated stock price (USD)')
