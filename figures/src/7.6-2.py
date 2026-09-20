theta=np.linspace(0,2*np.pi,300)
S=np.array([[0.0004,0.00024],[0.00024,0.0009]])
vals=np.linalg.eigvalsh(S)[::-1]
xy=np.vstack([np.sqrt(vals[0])*np.cos(theta),np.sqrt(vals[1])*np.sin(theta)])
ax.plot(xy[0]*100,xy[1]*100,color=ACCENT,lw=2)
ax.plot([-np.sqrt(vals[0])*100,np.sqrt(vals[0])*100],[0,0],color=BAD,ls='--',label='large eigen-direction')
ax.plot([0,0],[-np.sqrt(vals[1])*100,np.sqrt(vals[1])*100],color=WARM,ls=':',label='small eigen-direction')
ax.set_aspect('equal');ax.set_xlabel('rotated direction 1 (%)');ax.set_ylabel('rotated direction 2 (%)');ax.legend(loc='upper right')
ax.set_title('Covariance becomes diagonal along eigenvectors',fontsize=9,loc='left')
