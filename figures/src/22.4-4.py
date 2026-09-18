from scipy.stats import norm
rng=np.random.default_rng(7);n=5000;rho=0.7
z1=rng.standard_normal(n);z2=rho*z1+np.sqrt(1-rho**2)*rng.standard_normal(n)
tau=2/np.pi*np.arcsin(rho);th=1/(1-tau);a=1/th
U=rng.uniform(-np.pi/2,np.pi/2,n);W=rng.exponential(1,n)
V=np.sin(a*(U+np.pi/2))/np.cos(U)**(1/a)*(np.cos(U-a*(U+np.pi/2))/W)**((1-a)/a)
E=rng.exponential(1,(2,n));G=norm.ppf(np.exp(-(E/V)**a))
fig=ax.figure;gs=fig.add_gridspec(1,2);ax.set_subplotspec(gs[0]);ax2=fig.add_subplot(gs[1],sharex=ax,sharey=ax)
for A,(u,v),lab in ((ax,(z1,z2),'Bivariate normal'),(ax2,(G[0],G[1]),'Meta-Gumbel')):
    A.scatter(u,v,s=2,color=ACCENT,alpha=.35);A.axvline(2.5,color=BAD,lw=.8);A.axhline(2.5,color=BAD,lw=.8)
    k=int(((u>2.5)&(v>2.5)).sum());c=np.corrcoef(u,v)[0,1]
    A.set_title(f'{lab}: corr {c:.2f}, both above 2.5: {k}',loc='left',fontsize=8);A.grid(alpha=.2)
ax.set_xlim(-4,4.5);ax.set_ylim(-4,4.5);ax.set_xlabel('Asset 1');ax.set_ylabel('Asset 2');ax2.set_xlabel('Asset 1')
