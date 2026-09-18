labels=['Exact log','Milstein','Euler'];vals=[114.6599,114.5630,116.0809];ax.bar(labels,vals,color=[GOOD,ACCENT,BAD],width=.55);ax.set_ylim(112,117.2);ax.set_ylabel('Terminal price after 4 steps (USD/share)');ax.set_title('Same four shocks, three endpoints',loc='left');
for i,v in enumerate(vals):ax.text(i,v+.12,f'USD {v:.2f}',ha='center',fontsize=8)
