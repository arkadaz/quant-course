rng=np.random.default_rng(53);R=900
for j in range(36):
    fail=rng.random(R)<1/512;inc=np.where(fail,-511000,1000);eq=np.r_[0,np.cumsum(inc)]
    first=np.flatnonzero(fail);end=(first[0]+1) if len(first) else R
    ax.plot(np.arange(end+1),eq[:end+1]/1000,color=BAD if len(first) else ACCENT,alpha=0.28,lw=1)
ax.axhline(0,color=INK,lw=0.8);ax.set_xlabel('Completed cycles');ax.set_ylabel('Cumulative P&L (USD thousands)');ax.set_title('Fixed nine-rung policy; paths stop at first ladder failure',fontsize=9,loc='left')
