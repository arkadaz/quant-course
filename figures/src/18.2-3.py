bp=np.array([1,5,10,25,50]);loss=10_000_000*7.2*bp/10000
ax.bar([str(x) for x in bp],loss,color=BAD);ax.set_xlabel('Yield increase (bp)');ax.set_ylabel('Estimated loss (USD)');ax.set_title('Duration-only loss on USD 10M',loc='left')
