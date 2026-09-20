x=np.linspace(0,10,200); y=(10-x)/2
ax.plot(x,y,color=BAD,lw=2)
ax.annotate('',xy=(7,4),xytext=(6,2),arrowprops=dict(arrowstyle='->',color=ACCENT,lw=2))
ax.text(7.1,4.1,'normal a = (1, 2)',color=ACCENT,fontsize=8)
ax.set_xlim(-0.5,10.8);ax.set_ylim(-0.3,5.8);ax.set_xlabel('x1 (USD million)');ax.set_ylabel('x2 (USD million)')
ax.set_title('The coefficient vector is normal to the boundary',fontsize=9,loc='left')
