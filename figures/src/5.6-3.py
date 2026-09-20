rho,nu=0.6,4
lambda_gauss=0.0
lambda_t=2*stats.t.cdf(-np.sqrt((nu+1)*(1-rho)/(1+rho)),df=nu+1)
vals=[lambda_gauss,lambda_t]
ax.bar(['Gaussian copula','Student-t copula (df=4)'],vals,color=[ACCENT,BAD])
for i,v in enumerate(vals): ax.text(i,v+0.012,f'{v:.3f}',ha='center',fontsize=8,color=INK)
ax.set_ylim(0,0.38);ax.set_ylabel('upper-tail dependence coefficient')
ax.set_title('Same central rho, different asymptotic tail dependence',fontsize=9,loc='left')
