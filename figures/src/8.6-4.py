labels=['Full Σ SPX diagonal','Projected ΣX']
values=[0.0004,0.0004]
ax.bar(labels,values,color=[ACCENT,GOOD])
ax.set_ylabel('variance (return²/day²)');ax.set_ylim(0,0.00055)
for i,v in enumerate(values):ax.text(i,v+0.00002,f'{v:.4f}',ha='center',fontsize=8)
ax.set_title('Projection preserves the selected variance',fontsize=9,loc='left')
