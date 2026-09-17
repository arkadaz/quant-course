x=np.linspace(-2,2,180);y=np.linspace(-2,2,180);X,Y=np.meshgrid(x,y);Z=(X+Y)**2+.08*(X-Y)**2;levels=[.02,.08,.2,.5,1,2,4];cs=ax.contour(X,Y,Z,levels=levels,colors=SERIES);label_pos=[(.25,-.25),(-.5,.5),(.224,.224),(1.25,-1.25),(-.5,-.5),(.707,.707),(-1,-1)];
for level,pos in zip(levels,label_pos): ax.clabel(cs,levels=[level],manual=[pos],inline=True,fontsize=7,fmt='%.2f');
ax.set_xlabel('Transformed parameter 1');ax.set_ylabel('Transformed parameter 2');ax.set_aspect('equal')
