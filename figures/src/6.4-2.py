names=['Buy AAPL','Short JPM','Buy XOM']
vals=[1,1,1]
ax.bar(names,vals,color=[GOOD,BAD,GOOD],width=.55)
for i,v in enumerate(vals):ax.text(i,v+.05,'$1.0M',ha='center',fontsize=9,color=INK)
ax.set_ylim(0,1.35);ax.set_ylabel('Traded notional ($M)')
ax.set_title('L1 turnover adds the three tickets: $3.0M',loc='left')
