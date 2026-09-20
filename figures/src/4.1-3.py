rng=np.random.default_rng(51);n=80;t=np.arange(n+1)
for drift,col,label in [(0.12,GOOD,'submartingale'),(0.0,ACCENT,'martingale'),(-0.12,BAD,'supermartingale')]:
    inc=rng.normal(drift,1.0,size=(250,n));p=np.c_[np.zeros(250),np.cumsum(inc,axis=1)]
    ax.plot(t,p[:5].T,color=col,alpha=0.10,lw=0.8)
    ax.plot(t,p.mean(axis=0),color=col,lw=2.4,label=label)
ax.axhline(0,color=MUTED,lw=0.8);ax.set_xlabel('Time step');ax.set_ylabel('Value change');ax.legend(loc='upper left',ncol=3,fontsize=7)
