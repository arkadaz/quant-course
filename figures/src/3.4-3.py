rng=np.random.default_rng(144); n=100; se=.20; est=.08+rng.normal(0,se,n); lo=est-1.96*se; hi=est+1.96*se; cover=(lo<=.08)&(.08<=hi)
for i in range(n): ax.plot([lo[i],hi[i]],[i,i],color=GOOD if cover[i] else BAD,lw=.8)
ax.axvline(.08,color=INK,lw=1.2); ax.set(xlabel='Annual expected return',ylabel='Repeated samples',xlim=(-.75,.9)); ax.grid(alpha=.18)
