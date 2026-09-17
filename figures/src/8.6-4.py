vals=[.01247863,.01325];ax.bar(['Equality only','Long-only'],vals,color=[ACCENT,GOOD],width=.55)
for i,v in enumerate(vals):ax.text(i,v+.00012,f'{v:.6f}',ha='center',weight='bold');ax.set_ylim(0,.0145);ax.set_ylabel('Minimum annual variance');ax.set_title('A tighter feasible set cannot improve the minimum',loc='left')
