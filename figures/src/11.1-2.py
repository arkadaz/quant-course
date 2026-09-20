x=np.linspace(0,6,301);boundary=10.8-1.2*x;mask=(boundary<=6)&(boundary>=0)
ax.fill_between(x,np.maximum(boundary,0),6,where=mask,color=GOOD,alpha=.18)
ax.plot(x,boundary,color=ACCENT,lw=2,label='beta boundary')
for cost,col in [(1260,BAD),(1350,WARM),(1440,MUTED)]:
    ax.plot(x,(cost-180*x)/90,color=col,ls='--',lw=1.3,label=f'C = USD {cost:,}')
ax.scatter([4],[6],color=BAD,s=45,zorder=4)
ax.set_xlim(0,6.4);ax.set_ylim(0,6.4);ax.set_xlabel('Short QQQ, $x_Q$ (USD million)');ax.set_ylabel('Short SPY, $x_S$ (USD million)')
ax.legend(loc='lower left',fontsize=7);ax.set_title('The cheapest feasible contour selects the hedge',loc='left')
