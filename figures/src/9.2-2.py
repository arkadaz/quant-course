rng=np.random.default_rng(520);n=400;t=np.arange(n+1);noise=rng.normal(0,2500,size=(600,n));M=np.c_[np.zeros(600),np.cumsum(noise,axis=1)]
ax.plot(t,M[:12].T,color=ACCENT,alpha=0.13,lw=0.8);ax.plot(t,M.mean(axis=0),color=INK,lw=2.5,label='cross-path mean')
ax.axhline(0,color=WARM,ls='--',lw=1.2);ax.set_xlabel('Trade count');ax.set_ylabel('Centered P&L (USD)');ax.legend(loc='upper left')
