S0=K=50.;T=.25;r=.02;sig=.3;n_opt=1e5
def bs(S,tau):
    d1=(np.log(S/K)+(r+.5*sig**2)*tau)/(sig*np.sqrt(tau))
    return S*stats.norm.cdf(d1)-K*np.exp(-r*tau)*stats.norm.cdf(d1-sig*np.sqrt(tau)),stats.norm.cdf(d1)
def run(N,sig_true,M=4000):
    rng=np.random.default_rng(1);dt=T/N
    S=np.full(M,S0);C0,dl=bs(S0,T);V=np.full(M,C0*n_opt);H=dl*n_opt;B=V-H*S
    for i in range(1,N+1):
        S=S*np.exp((r-.5*sig_true**2)*dt+sig_true*np.sqrt(dt)*rng.standard_normal(M))
        V=H*S+B*np.exp(r*dt)
        if i<N:
            _,dl=bs(S,T-i*dt);H=dl*n_opt;B=V-H*S
    return (V-n_opt*np.maximum(S-K,0))/1000
bins=np.linspace(-250,250,101)
for N,c in ((10,WARM),(50,ACCENT),(250,GOOD)):
    pl=run(N,.3);ax.hist(pl,bins=bins,histtype='step',lw=1.8,color=c,label=f'{N} rebalances, sd {pl.std():.0f}k')
pl=run(50,.25);ax.hist(pl,bins=bins,histtype='step',lw=1.4,ls=(0,(4,2)),color=BAD,label=f'50, true vol 25%: mean +{pl.mean():.0f}k')
ax.axvline(55.394,color=INK,lw=1,ls=':');ax.text(58,ax.get_ylim()[1]*.9,'source path +55.4k',fontsize=7.3)
ax.set_xlabel('Hedging P&L on 100,000 calls (USD thousand)');ax.set_ylabel('Paths out of 4,000')
ax.set_title('More rebalancing shrinks the error; wrong vol shifts it',loc='left');ax.legend(fontsize=7,loc='upper left');ax.grid(alpha=.2)
