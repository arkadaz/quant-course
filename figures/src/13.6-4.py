
vals=np.array([.398443914,.241165374,.024176827,-.157278540,.082168479]);names=['Straddle','Strangle','Risk reversal','Butterfly','Calendar']
ax.bar(names,vals,color=np.where(vals>=0,ACCENT,BAD));ax.axhline(0,color=INK,lw=1);ax.set_ylabel('Vega (USD per vol point)');ax.tick_params(axis='x',rotation=15)
