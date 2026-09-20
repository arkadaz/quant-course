x=np.linspace(-1.1,1.1,180);y=np.linspace(-1.1,1.1,180);X,Y=np.meshgrid(x,y);Z=.04*X**2+.012*X*Y+.01*Y**2
ax.contour(X,Y,Z,levels=9,cmap='viridis');ax.scatter([0],[0],color=GOOD,s=45);ax.set_xlabel('$p_1$');ax.set_ylabel('$p_2$');ax.set_aspect('equal');ax.set_title('Positive curvature leaves one basin',loc='left')
