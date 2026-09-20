s=np.linspace(470,570,500);k=520;prem=21.72;pay=np.abs(s-k);pnl=pay-prem
ax.plot(s,pay,color=ACCENT,lw=2,label='expiry payoff');ax.plot(s,pnl,color=GOOD,lw=2,label='buyer P&L after premium')
ax.axhline(0,color=INK,lw=.8);ax.axvline(k,color=MUTED,ls='--',lw=1,label='strike = spot')
ax.scatter([k-prem,k+prem],[0,0],color=BAD,s=30,zorder=4,label='break-even')
ax.set_xlabel('SPY price at expiry (USD)');ax.set_ylabel('USD per share');ax.set_title('30-day ATM straddle: two-sided exposure',loc='left');ax.legend(loc='upper center',ncol=2,fontsize=7)
