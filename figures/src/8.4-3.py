theta=np.linspace(0,2*np.pi,300)
for rho,col,label in [(0.0,MUTED,'rho = 0'),(0.4,BAD,'rho = 0.4 target')]:
    z=np.vstack([2.0*np.cos(theta),3.0*(rho*np.cos(theta)+np.sqrt(1-rho*rho)*np.sin(theta))])
    ax.plot(z[0]+0.04,z[1]+0.03,color=col,lw=2,label=label)
ax.scatter([0.04],[0.03],color=INK,s=20,label='mean')
ax.set_aspect('equal');ax.set_xlabel('SPX return (%)');ax.set_ylabel('QQQ return (%)');ax.legend(loc='upper left')
ax.set_title('Correlation rotates the equal-distance ellipse',fontsize=9,loc='left')
