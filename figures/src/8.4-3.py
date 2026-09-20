n=30;j=np.arange(n+1);share=(j+1)/(n+2);polya=np.full(n+1,1/(n+1));coin=stats.binom.pmf(j,n,0.5)
ax.bar(share-0.006,polya,width=0.012,color=ACCENT,alpha=0.75,label="Polya urn")
ax.bar(j/n+0.006,coin,width=0.012,color=WARM,alpha=0.65,label='independent coin')
ax.set_xlabel('Red share');ax.set_ylabel('Probability mass');ax.set_xlim(0,1);ax.legend(loc='upper left')
