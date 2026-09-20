mu=np.array([0.0004,0.0003])*100;S=np.array([[0.0004,0.00024],[0.00024,0.0009]])*10000
x=np.linspace(-8,8,240);y=np.linspace(-10,10,240);X,Y=np.meshgrid(x,y)
Z=stats.multivariate_normal(mean=mu,cov=S).pdf(np.dstack((X,Y)))
ax.contourf(X,Y,Z,levels=12,cmap='Blues',alpha=0.8)
marg=stats.norm.pdf(x,loc=mu[0],scale=np.sqrt(S[0,0]));base=y.min()+0.25
proj=base+1.8*marg/marg.max();ax.plot(x,proj,color=BAD,lw=2,label='SPX marginal, centered at 0.04%')
ax.fill_between(x,base,proj,color=BAD,alpha=.15)
ax.set_xlabel('SPX return (%)');ax.set_ylabel('QQQ return (%)');ax.legend(loc='upper left',fontsize=7)
ax.set_title('Integrating out QQQ leaves the SPX marginal',fontsize=9,loc='left')
