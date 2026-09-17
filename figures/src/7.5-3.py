rng=np.random.default_rng(0)
mu=np.array([0.0004,0.0003]);S=np.array([[0.0004,0.00024],[0.00024,0.0009]])
z=rng.multivariate_normal(mu,S,5000)
for a,col,label in [(np.array([1,0]),ACCENT,'SPX'),(np.array([0,1]),WARM,'QQQ'),(np.array([0.6,0.4]),GOOD,'0.6 SPX + 0.4 QQQ')]:
    L=z@a;ax.hist(L*100,bins=48,density=True,histtype='step',lw=1.8,color=col,label=label)
ax.set_xlabel('portfolio return (%)');ax.set_ylabel('density');ax.legend(loc='upper left',fontsize=8)
ax.set_title('Every displayed linear combination is Normal',fontsize=9,loc='left')
