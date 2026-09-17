k=np.arange(1,10);stake=1000*2**(k-1);loss=1000*(2**k-1)
ax.plot(k,stake/1000,marker='o',color=ACCENT,label='next stake');ax.plot(k,loss/1000,marker='s',color=BAD,label='cumulative loss')
ax.axhline(1,color=GOOD,ls='--',label='target profit = $1k');ax.set_yscale('log',base=2);ax.set_xlabel('Ladder rung');ax.set_ylabel('USD thousands, log2 scale');ax.set_xticks(k);ax.legend(loc='upper left',ncol=2,fontsize=7)
