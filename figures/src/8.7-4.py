etas=np.array([.0001,.0005,.0013,.0020]);labels=['slow','stable','oscillatory','divergent'];factor=np.abs(1-etas*1527.16)
ax.bar(labels,factor,color=[MUTED,GOOD,WARM,BAD]);ax.axhline(1,color=INK,ls='--',label='error no longer contracts');ax.set_ylabel('Local error multiplier');ax.legend();ax.set_title('Step size controls local stability',loc='left')
