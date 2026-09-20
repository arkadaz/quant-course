
kv=.04020277169244778;nv=1e6;vol=np.linspace(0,.4,301);pnl=nv*(vol**2-kv)
ax.plot(100*vol,pnl,color=ACCENT);ax.axhline(0,color=INK,lw=1);ax.axvline(100*np.sqrt(kv),color=GOOD,ls='--',label='Fair strike')
rv=np.sqrt(.04788);ax.scatter([100*rv],[nv*(rv**2-kv)],color=BAD,zorder=3,label='Worked path')
ax.set_xlabel('Realized volatility (%)');ax.set_ylabel('Long-variance payoff (USD)');ax.legend()
