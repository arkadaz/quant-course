labels=['Itô left point','right point'];vals=[0,1];ax.bar(labels,vals,color=[GOOD,BAD],width=.55);ax.axhline(0,color=INK,lw=.8);ax.set_ylabel('Cumulative gain (risk units)');ax.set_title('One index shift manufactures one unit of gain',loc='left');
for i,v in enumerate(vals):ax.text(i,v+.04,f'{v:.2f}',ha='center',weight='bold')
