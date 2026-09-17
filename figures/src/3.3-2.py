labels=['AAPL/JPM common','AAPL vs JPM','XOM only']
vals=[5.5,.5,4.0]
ax.bar(labels,vals,color=[ACCENT,WARM,GOOD],width=.58)
for i,v in enumerate(vals): ax.text(i,v+.18,f'${v:.1f}M',ha='center',fontsize=9,color=INK)
ax.set_ylim(0,6.5);ax.set_ylabel('Basis coordinate ($M)')
ax.tick_params(axis='x',rotation=12)
ax.set_title('Coordinates reveal the risk story hidden by tickers',loc='left')
