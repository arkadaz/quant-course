x=np.linspace(-2.8,2.0,260);y=np.linspace(-1.4,2.2,260);X,Y=np.meshgrid(x,y);Z=X**2+3*X*Y+Y**3
ax.contour(X,Y,Z,levels=np.linspace(-5,5,17),cmap='coolwarm');ax.scatter([0],[0],color=BAD,s=48,label='saddle A');ax.scatter([-2.25],[1.5],color=GOOD,s=48,label='local min B')
ax.set_xlabel('$x_1$');ax.set_ylabel('$x_2$');ax.legend();ax.set_title('Zero gradient does not choose the geometry',loc='left')
