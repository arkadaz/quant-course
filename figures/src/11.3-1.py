labels=['Primal optimum','Dual optimum'];vals=[1260,1260]
ax.bar(labels,vals,color=[ACCENT,GOOD],width=.52)
for i,v in enumerate(vals):ax.text(i,v+35,f'USD {v:,}',ha='center',fontsize=11,weight='bold')
ax.set_ylim(0,1450);ax.set_ylabel('Objective value (USD)')
ax.set_title('Strong duality: both ledgers close at the same value',loc='left')
