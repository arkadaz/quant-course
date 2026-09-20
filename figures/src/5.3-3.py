y=np.linspace(-5,5,100);sx,sy,rho=2.5,3.0,0.6
mean=rho*sx/sy*y
ax.plot(y,mean,color=ACCENT,lw=2)
ax.scatter([-3,0,3],[-1.5,0,1.5],color=[BAD,MUTED,GOOD],zorder=3)
ax.axhline(0,color=MUTED,lw=0.8);ax.axvline(0,color=MUTED,lw=0.8)
ax.set_xlabel('observed MSFT return (%)');ax.set_ylabel('conditional mean AAPL return (%)')
ax.set_title('Conditional expectation translates a signal into a forecast',fontsize=9,loc='left')
