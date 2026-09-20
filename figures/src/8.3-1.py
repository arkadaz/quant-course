rng=np.random.default_rng(0)
xh=rng.normal(0,1,350);eps=0.08*rng.normal(size=350)
x=np.r_[xh,-xh];y=np.r_[xh*xh+eps,xh*xh+eps];sample_cov=np.cov(x,y,ddof=1)[0,1]
ax.scatter(x,y,s=9,alpha=0.35,color=ACCENT)
ax.axvline(0,color=MUTED,lw=0.7);ax.text(-3.5,8.5,f'sample covariance = {sample_cov:.2e}',fontsize=8,color=INK)
ax.set_xlabel('signal X');ax.set_ylabel('response Y')
ax.set_title('Zero covariance can hide a strong nonlinear U-shape',fontsize=9,loc='left')
