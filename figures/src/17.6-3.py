d=np.linspace(0,30,301);a=np.where(d<10,1,np.where(d<20,.5,0));ax.step(d,a,where='post');ax.set_xlabel('Observed drawdown (%)');ax.set_ylabel('Next-day risk fraction');ax.set_ylim(-.05,1.1)
