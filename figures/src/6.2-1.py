x=np.linspace(-6,6,160);y=np.linspace(-8,8,200);X,Y=np.meshgrid(x,y)
sx,sy,rho=2.5,3.0,0.6;cov=[[sx**2,rho*sx*sy],[rho*sx*sy,sy**2]]
Z=stats.multivariate_normal.pdf(np.dstack((X,Y)),mean=[0,0],cov=cov)
yi=np.linspace(-18,18,500);XI,YI=np.meshgrid(x,yi);ZI=stats.multivariate_normal.pdf(np.dstack((XI,YI)),mean=[0,0],cov=cov)
ax.contourf(X,Y,Z,levels=10,cmap='Blues')
mx=np.trapezoid(ZI,yi,axis=0);baseline=-8;shown=baseline+1.8*mx/mx.max()
ax.plot(x,shown,color=BAD,lw=2,label='AAPL marginal shape (rescaled)')
ax.set_xlabel('AAPL return (%)');ax.set_ylabel('MSFT return (%)')
ax.legend(loc='upper left');ax.set_title('Integrate down the other axis to get a marginal',fontsize=9,loc='left')
