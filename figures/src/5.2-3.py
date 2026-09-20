y=np.linspace(-12,12,500);x0=0.0;sx,sy,rho=2.5,3.0,0.6
cov=[[sx**2,rho*sx*sy],[rho*sx*sy,sy**2]]
points=np.column_stack([np.full_like(y,x0),y])
slice_=stats.multivariate_normal.pdf(points,mean=[0,0],cov=cov)
area=np.trapezoid(slice_,y);exact=stats.norm.pdf(x0,0,sx)
ax.fill_between(y,0,slice_,color=GOOD,alpha=0.35);ax.plot(y,slice_,color=GOOD,lw=2)
ax.text(-11,0.047,f'slice area = {area:.4f}\nf_X(0) = {exact:.4f}',fontsize=8,color=INK)
ax.set_xlabel('MSFT return (%) at AAPL = 0%');ax.set_ylabel('joint density per percentage point²')
ax.set_title('A whole hidden-axis slice integrates to one marginal height',fontsize=9,loc='left')
