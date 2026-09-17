x=np.linspace(-12,12,400);sx,sy=2.5,3.0
Fx=stats.norm.cdf(x,0,sx);Fy=stats.norm.cdf(x,0,sy)
ax.plot(x,Fx,color=ACCENT,lw=2,label='AAPL CDF')
ax.plot(x,Fy,color=WARM,lw=2,label='MSFT CDF')
ax.axhline(1,color=MUTED,ls='--',lw=0.8)
ax.set_xlabel('return threshold (%)');ax.set_ylabel('cumulative probability')
ax.legend(loc='upper left');ax.set_title('Marginal CDFs approach probability one',fontsize=9,loc='left')
