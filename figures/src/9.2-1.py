rng=np.random.default_rng(621);n=800;m=8;t=np.linspace(0,1,n+1);dw=rng.normal(0,np.sqrt(1/n),(m,n));w=np.c_[np.zeros(m),np.cumsum(dw,axis=1)]
for i in range(m):ax.plot(t,w[i],color=SERIES[i%len(SERIES)],alpha=.62,lw=1)
ax.plot(t,np.sqrt(t),color=INK,ls='--',lw=1.2,label=r'$+\sqrt{t}$')
ax.plot(t,-np.sqrt(t),color=INK,ls='--',lw=1.2,label=r'$-\sqrt{t}$')
ax.set_xlabel('Time');ax.set_ylabel('$W_t$');ax.set_title('Standard Brownian motion sample paths',loc='left');ax.legend(loc='lower left',ncol=2)
