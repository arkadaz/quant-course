q=np.linspace(0.01,0.5,80);rho=0.6
z=stats.norm.ppf(q);rng=np.random.default_rng(0)
product=q*q
joint=np.array([stats.multivariate_normal.cdf([zi,zi],mean=[0,0],cov=[[1,rho],[rho,1]],rng=rng) for zi in z])
ax.plot(q,product,color=ACCENT,lw=2,label='independent: q²')
ax.plot(q,joint,color=BAD,lw=2,label='Gaussian copula: rho=0.6')
ax.set_xlabel('marginal lower-tail probability q')
ax.set_ylabel('joint lower-tail probability')
ax.legend(loc='upper left');ax.set_title('Dependence changes joint tail probability',fontsize=9,loc='left')
