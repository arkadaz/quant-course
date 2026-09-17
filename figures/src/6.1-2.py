x=np.linspace(-6,6,160);y=np.linspace(-6,6,160);X,Y=np.meshgrid(x,y)
sx,sy,rho=2.5,3.0,0.6
Z=np.exp(-0.5/(1-rho**2)*((X/sx)**2-2*rho*X*Y/(sx*sy)+(Y/sy)**2))/(2*np.pi*sx*sy*np.sqrt(1-rho**2))
cs=ax.contour(X,Y,Z,levels=7,colors=ACCENT)
ax.clabel(cs,inline=True,fontsize=7,fmt='%.3f')
ax.set_xlabel('AAPL return (%)');ax.set_ylabel('MSFT return (%)')
ax.set_title('Joint PDF contours show co-movement geometry',fontsize=9,loc='left')
