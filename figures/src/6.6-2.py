rng=np.random.default_rng(0)
for rho,col in [(0.0,GOOD),(0.5,ACCENT),(0.9,BAD)]:
    z=rng.multivariate_normal([0,0],[[1,rho],[rho,1]],500)
    ax.scatter(z[:,0],z[:,1],s=5,alpha=0.18,color=col,label=f'rho = {rho}')
ax.set_xlabel('latent variable 1');ax.set_ylabel('latent variable 2');ax.legend(loc='upper left',ncol=3)
ax.set_title('Gaussian copula dependence strengthens as rho rises',fontsize=9,loc='left')
