n=20
k=np.arange(n+1)
prob=stats.binom.pmf(k,n,0.6)
ax.bar(k,prob,color=ACCENT)
ax.axvline(12,color=BAD,ls='--',lw=1.5,label='mean = np = 12')
ax.set_xlabel('marketable orders among 20')
ax.set_ylabel('conditional probability')
ax.legend(loc='upper left')
ax.set_title('Before averaging over N, the split is Binomial',fontsize=9,loc='left')
