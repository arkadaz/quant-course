x=np.array([0,1,2,4,5,6])
labels=['AAPL','JPM','XOM','common\nAAPL+JPM','relative\nAAPL-JPM','XOM only']
vals=[6,5,4,5.5,.5,4]
colors=[ACCENT,ACCENT,ACCENT,WARM,WARM,WARM]
ax.bar(x,vals,color=colors,width=.68)
for i,v in zip(x,vals): ax.text(i,v+.18,f'${v:.1f}M',ha='center',fontsize=8,color=INK)
ax.axvline(3,color=MUTED,lw=.9,ls='--')
ax.text(1,6.55,'ticker-basis coordinates x',ha='center',fontsize=8,color=ACCENT)
ax.text(5,6.55,'risk-basis coordinates c',ha='center',fontsize=8,color=WARM)
ax.set_xticks(x,labels);ax.set_ylim(0,7.2);ax.set_ylabel('Coordinate value (USD millions)')
ax.tick_params(axis='x',labelsize=7)
ax.set_title('Same position, two separate coordinate systems',loc='left')
