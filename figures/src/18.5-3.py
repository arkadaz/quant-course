labels=['half-spread','impact','fee','one leg','round trip','gross alpha']
vals=[15,72,8,95,190,42]
cols=[WARM,BAD,MUTED,INK,BAD,GOOD]
x=np.arange(len(vals))
ax.bar(x,vals,color=cols,width=.6)
for i,v in enumerate(vals):
    ax.text(i,v+3,f'{v} bp',ha='center',fontsize=8)
ax.axhline(42,color=GOOD,lw=1,ls=(0,(4,3)))
ax.text(2.6,125,'net -148 bp per round',fontsize=7.5,color=BAD)
ax.set_xticks(x);ax.set_xticklabels(labels,rotation=15);ax.set_ylim(0,215)
ax.set_ylabel('Basis points of a 200M USD order')
ax.set_title('Cost stack of one round vs the 42 bp the backtest promised',loc='left');ax.grid(axis='y',alpha=.2)
