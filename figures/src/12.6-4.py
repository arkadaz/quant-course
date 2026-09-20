vals=[.0092822,.0095789];ax.bar(['Shorting allowed','Long-only'],vals,color=[ACCENT,GOOD],width=.55)
for i,(v,s) in enumerate(zip(vals,['9.634%','9.787%'])):ax.text(i,v+.00015,f'{v:.7f}  ($\\sigma$ {s})',ha='center',weight='bold')
ax.set_ylim(0,.0112);ax.set_ylabel('Minimum annual variance');ax.set_title('A tighter feasible set cannot improve the minimum',loc='left')
