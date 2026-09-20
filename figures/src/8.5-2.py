t=np.linspace(-0.003,0.003,200);mu=75;sig=300
M=np.exp(mu*t+0.5*sig*sig*t*t)
ax.plot(t,M,color=ACCENT,lw=2)
ax.plot(t,1+mu*t,color=GOOD,ls='--',label='tangent: mean')
ax.scatter([0],[1],color=BAD,zorder=3,label='t = 0')
ax.set_xlabel('t (day/USD)');ax.set_ylabel('MGF value')
ax.legend(loc='upper left');ax.set_title('Local slope and curvature encode moments',fontsize=9,loc='left')
