rng=np.random.default_rng(52);n=400;t=np.arange(n+1);baseline=320*t
raw=np.r_[0,np.cumsum(rng.normal(0,2500,400))];bridge=raw-(t/400)*raw[-1]+(t/400)*37000
observed=baseline+bridge
ax.plot(t,observed,color=ACCENT,label='observed cumulative P&L')
ax.plot(t,baseline,color=WARM,ls='--',label='baseline: $320 per trade')
ax.vlines(400,128000,165000,color=GOOD,lw=3);ax.text(392,146500,'excess = $37,000',ha='right',va='center',color=GOOD)
ax.scatter([400],[165000],color=ACCENT,s=30);ax.set_xlabel('Trade count');ax.set_ylabel('USD');ax.legend(loc='upper left')
