x=np.linspace(-10,8,400);y0=-3.0;sx,sy,rho=2.5,3.0,0.6
mean=rho*sx/sy*y0;sd=sx*np.sqrt(1-rho**2)
cond=stats.norm.pdf(x,mean,sd);area=np.trapezoid(cond,x)
ax.fill_between(x,0,cond,color=ACCENT,alpha=0.25);ax.plot(x,cond,color=ACCENT,lw=2,label=f'normalized slice, area={area:.3f}')
ax.axvline(mean,color=BAD,ls='--',lw=1,label=f'conditional mean={mean:.1f}%')
ax.set_xlabel('AAPL return (%) | MSFT = -3%');ax.set_ylabel('conditional density per percentage point')
ax.legend(loc='upper right');ax.set_title('Observed MSFT return selects and normalizes an AAPL slice',fontsize=9,loc='left')
