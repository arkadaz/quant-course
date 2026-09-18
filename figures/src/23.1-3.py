labels=['invest today','hold the right\nto wait two years'];vals=[1.0,2.6392]
ax.bar([0,1],vals,color=[MUTED,ACCENT],width=.55)
for i,v in enumerate(vals):
    ax.text(i,v+.07,f'{v:.4f}',ha='center',fontsize=8.5)
ax.annotate('',xy=(1.36,2.6392),xytext=(1.36,1.0),arrowprops=dict(arrowstyle='<->',color=GOOD,lw=1.2))
ax.plot([0.28,1.36],[1.0,1.0],color=GOOD,lw=.8,ls=(0,(3,3)))
ax.text(1.40,1.80,'flexibility\n1.6392',fontsize=8,color=GOOD,va='center')
ax.set_xticks([0,1]);ax.set_xticklabels(labels);ax.set_xlim(-.5,1.85)
ax.set_ylabel('Value today (USD M)');ax.set_ylim(0,3.1)
ax.set_title('Same project, two ways to hold it',loc='left');ax.grid(axis='y',alpha=.2)
