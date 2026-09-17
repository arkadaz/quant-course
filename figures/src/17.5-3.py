rng=np.random.default_rng(175)
z=rng.normal(size=(20000,12));dt=1/12
s=100*np.exp(np.cumsum((.03-.5*.2**2)*dt+.2*np.sqrt(dt)*z,axis=1))
x=np.exp(-.03)*np.maximum(s.mean(axis=1)-100,0)
y=np.exp(-.03)*s[:,-1]
ax.scatter(y[:600],x[:600],s=7,alpha=.25);ax.set_xlabel('Discounted terminal stock (USD)');ax.set_ylabel('Discounted Asian payoff (USD)')
