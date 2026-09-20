R=np.arange(0,2001);s=(511/512)**R;ax.plot(R,s,color=ACCENT);ax.axhline(0.5,color=MUTED,ls='--');ax.axvline(354.54,color=WARM,ls='--',label='half-life = 354.54 cycles')
for r in [100,500,2000]:ax.scatter([r],[(511/512)**r],color=BAD,s=24);ax.text(r,(511/512)**r+0.04,f'{100*(511/512)**r:.1f}%',ha='center',fontsize=8)
ax.set_xlabel('Cycles');ax.set_ylabel('Probability of no ladder failure');ax.set_ylim(0,1.05);ax.legend(loc='upper right')
