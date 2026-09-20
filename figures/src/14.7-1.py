
t=np.linspace(.001,3,300);v0=.09;th=.04;k=.2*10
mean=th+(v0-th)*np.exp(-k*t);avg=th+(v0-th)*(1-np.exp(-k*t))/(k*t)
ax.plot(t,mean,color=ACCENT,label='Expected instantaneous variance');ax.plot(t,avg,'--',color=WARM,label='Expected running average')
ax.axhline(th,color=MUTED,ls=':',label='Long-run variance');ax.set_xlabel('Horizon (years)');ax.set_ylabel('Variance (per year)');ax.legend()
