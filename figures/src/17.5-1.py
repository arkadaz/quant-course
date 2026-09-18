rng=np.random.default_rng(175)
z=rng.normal(size=(20000,12));dt=1/12
drift=(.02-.5*.3**2)*dt;shock=.3*np.sqrt(dt)
s=100*np.exp(np.cumsum(drift+shock*z,axis=1))
for row in s[:12]:ax.plot(np.arange(13),np.r_[100,row],alpha=.65,lw=1)
ax.set_xlabel('Month');ax.set_ylabel('Simulated stock price (USD)')
