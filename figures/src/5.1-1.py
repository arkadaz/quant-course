x=np.linspace(0,6,301)
boundary=10.8-1.2*x
mask=(boundary<=6)&(boundary>=0)
ax.fill_between(x,np.maximum(boundary,0),6,where=mask,color=GOOD,alpha=.24,label='feasible region')
ax.plot(x,boundary,color=ACCENT,lw=2,label='$1.2x_Q+x_S=10.8$')
ax.axvline(6,color=WARM,ls='--',lw=1);ax.axhline(6,color=WARM,ls='--',lw=1)
ax.scatter([4],[6],color=BAD,s=45,zorder=4,label='optimum (4, 6)')
ax.set_xlim(0,6.4);ax.set_ylim(0,6.4);ax.set_xlabel('Short QQQ, $x_Q$ (USD million)');ax.set_ylabel('Short SPY, $x_S$ (USD million)')
ax.legend(loc='lower left',fontsize=7);ax.set_title('Risk floor and liquidity caps define the feasible triangle',loc='left')
