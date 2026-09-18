rng=np.random.default_rng(175)
z=rng.normal(size=(20000,12));dt=1/12
drift=(.02-.5*.3**2)*dt;shock=.3*np.sqrt(dt)
s=100*np.exp(np.cumsum(drift+shock*z,axis=1))
x=np.exp(-.02)*np.maximum(s.mean(axis=1)-100,0)
y=np.exp(-.02)*s[:,-1]
ax.scatter(y[:600],x[:600],s=7,alpha=.25);ax.set_xlabel('Discounted terminal stock (USD)');ax.set_ylabel('Discounted Asian payoff (USD)')
