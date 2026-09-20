mu=np.array([0.0004,0.0003])*100
S=np.array([[0.0004,0.00024],[0.00024,0.0009]])*10000
x=np.linspace(-8,8,180);y=np.linspace(-10,10,180);X,Y=np.meshgrid(x,y)
pos=np.dstack((X,Y));Z=stats.multivariate_normal(mean=mu,cov=S).pdf(pos)
cs=ax.contour(X,Y,Z,levels=8,colors=ACCENT)
ax.clabel(cs,inline=True,fontsize=7,fmt='%.3f')
ax.scatter([mu[0]],[mu[1]],color=BAD,s=25)
ax.set_xlabel('SPX return (%)');ax.set_ylabel('QQQ return (%)')
ax.set_title('Contours are constant Mahalanobis distance',fontsize=9,loc='left')
