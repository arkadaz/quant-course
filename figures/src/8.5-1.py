t=np.linspace(-0.004,0.004,200);mu=75;sig=300
M=np.exp(mu*t+0.5*sig*sig*t*t)
ax.plot(t,M,color=ACCENT,lw=2)
ax.scatter([0],[1],color=BAD,zorder=3)
ax.annotate('M(0) = 1',(0,1),xytext=(0.0006,1.35),fontsize=8)
ax.axvline(0,color=MUTED,ls='--',lw=0.8)
ax.set_xlabel('t (day/USD)');ax.set_ylabel('M_X(t)')
ax.set_title('The MGF stores moments around t = 0',fontsize=9,loc='left')
