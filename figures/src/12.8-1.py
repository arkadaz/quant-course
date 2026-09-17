labels=['Exact log','Milstein','Euler'];vals=[224.3746875,224.3608836,227.755385];ax.bar(labels,vals,color=[GOOD,ACCENT,BAD],width=.55);ax.set_ylim(215,231);ax.set_ylabel('AAPL terminal price (USD/share)');ax.set_title('A coarse grid exposes pathwise error',loc='left');
for i,v in enumerate(vals):ax.text(i,v+.35,f'USD {v:.2f}',ha='center',fontsize=8)
