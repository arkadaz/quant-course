vals=[570.60,570.00];labs=['P: real-world forecast','Q: pricing forecast'];cols=[WARM,ACCENT]
ax.bar(labs,vals,color=cols,width=0.55);ax.axhline(570,color=INK,ls='--',lw=1.2,label='current price $570')
ax.set_ylim(569.4,571.0);ax.set_ylabel('One-step expectation (USD)')
for i,v in enumerate(vals):ax.text(i,v+0.05,f'${v:,.2f}',ha='center',fontsize=9)
ax.legend(loc='upper right');ax.tick_params(axis='x',labelrotation=0)
