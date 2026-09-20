rng=np.random.default_rng(633);m=5000;n=250;t=np.linspace(0,1,n+1);w=np.c_[np.zeros(m),np.cumsum(rng.normal(0,np.sqrt(1/n),(m,n)),axis=1)]
ax.plot(t,(w*w).mean(axis=0),color=ACCENT,lw=2,label='mean of $W_t^2$')
ax.plot(t,(w*w-t).mean(axis=0),color=GOOD,lw=2,label='mean of $W_t^2-t$')
ax.plot(t,t,color=INK,ls='--',lw=1,label='theory: $t$')
ax.axhline(0,color=MUTED,lw=.8);ax.set_xlabel('Time');ax.set_ylabel('Ensemble mean');ax.set_title('Compensation subtracts predictable quadratic growth',loc='left');ax.legend(loc='upper left')
