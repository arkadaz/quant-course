rng=np.random.default_rng(612);d=rng.normal(0,1,1200)
x=d[:-1];y=d[1:];rho=np.corrcoef(x,y)[0,1]
ax.scatter(x,y,s=8,alpha=.28,color=ACCENT,edgecolors='none')
ax.axhline(0,color=MUTED,lw=.8);ax.axvline(0,color=MUTED,lw=.8)
ax.set_xlabel('Increment $i$');ax.set_ylabel('Increment $i+1$');ax.set_title(f'Independent increments: sample correlation = {rho:.3f}',loc='left')
