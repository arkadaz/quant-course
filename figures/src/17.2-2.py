rng=np.random.default_rng(172);wins=rng.random(200)<.55
for f,col in [(.05,GOOD),(.1,ACCENT)]:
 w=np.r_[1e6,1e6*np.cumprod(np.where(wins,1+f,1-f))];ax.plot(w/1e6,color=col,label=f'f={f:.0%}')
ax.set_xlabel('Simulated round');ax.set_ylabel('Wealth (USD million)');ax.legend()
