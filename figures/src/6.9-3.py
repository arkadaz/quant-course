rng=np.random.default_rng(0)
xh=rng.normal(0,1,250);eps=0.08*rng.normal(size=250)
x=np.r_[xh,-xh];y=np.r_[xh*xh+eps,xh*xh+eps]
line=np.linspace(-3,3,180);coef=np.polyfit(x,y,1)
ax.scatter(x,y,s=8,alpha=0.25,color=MUTED)
ax.plot(line,np.polyval(coef,line),color=GOOD,lw=2,label=f'linear fit: slope {coef[0]:.2e}')
ax.plot(line,line*line,color=BAD,lw=2,label='quadratic structure')
ax.set_xlabel('signal X');ax.set_ylabel('response Y');ax.legend(loc='upper center')
ax.set_title('Zero linear slope is not zero dependence',fontsize=9,loc='left')
