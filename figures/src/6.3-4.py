x=np.linspace(-12,12,500);sx,sy,rho=2.5,3.0,0.6;sd=sx*np.sqrt(1-rho**2)
ys=np.array([-3.0,0.0,3.0]);means=rho*sx/sy*ys
curves=[stats.norm.pdf(x,m,sd) for m in means]
areas=[np.trapezoid(z,x) for z in curves]
ax.bar(['MSFT -3%','MSFT 0%','MSFT +3%'],areas,color=[BAD,MUTED,GOOD])
ax.axhline(1,color=ACCENT,ls='--',lw=1.2,label='required area = 1')
ax.set_ylim(0,1.12);ax.set_ylabel('conditional density area')
ax.legend(loc='lower left');ax.set_title('Every conditioned density renormalizes to one',fontsize=9,loc='left')
