rng=np.random.default_rng(0)
mu=np.array([0.0004,0.0003]);S=np.array([[0.0004,0.00024],[0.00024,0.0009]]);L=np.linalg.cholesky(S)
z=rng.normal(size=(5000,2));r=mu+z@L.T
vals=np.array([r[:,0].mean(),r[:,1].mean(),r[:,0].std(ddof=1),r[:,1].std(ddof=1)])*100
targets=np.array([mu[0],mu[1],np.sqrt(S[0,0]),np.sqrt(S[1,1])])*100
labels=['SPX mean','QQQ mean','SPX SD','QQQ SD']
ax.bar(labels,vals,color=[ACCENT,WARM,ACCENT,WARM],alpha=.8,label='simulation')
ax.scatter(range(4),targets,color=BAD,zorder=3,label='target')
ax.axhline(0,color=MUTED,lw=0.8)
ax.set_ylabel('daily return (%)');ax.legend(loc='upper left',fontsize=8)
ax.set_title('Simulation should reproduce target means and spreads',fontsize=9,loc='left')
