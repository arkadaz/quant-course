vals=[.0528,.0152];ax.bar(['SPY','AGG'],vals,color=[BAD,GOOD],width=.55)
for i,v in enumerate(vals):ax.text(i,v+.0015,f'{v:.4f}',ha='center',weight='bold')
ax.set_ylim(0,.06);ax.set_ylabel('Marginal annual variance');ax.set_title('Marginal risk depends on current holdings',loc='left')
