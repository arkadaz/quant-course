X={(0,0):10.0,(1,1):14.0,(1,0):8.0,(2,2):19.6,(2,1):11.2,(2,0):6.4}
V={(0,0):2.6392,(1,1):5.4286,(1,0):0.8730,(2,2):10.6,(2,1):2.2,(2,0):0.0}
for (t,k),x in X.items():
    if t<2:
        for kk in (k+1,k):
            ax.plot([t,t+1],[x,X[(t+1,kk)]],color=MUTED,lw=1.2,zorder=1)
ax.axhline(9.0,color=BAD,lw=1,ls=(0,(4,3)))
ax.text(2.05,8.2,'I = 9.0',fontsize=8,color=BAD)
for (t,k),x in X.items():
    ax.scatter([t],[x],s=42,color=ACCENT if V[(t,k)]>0 else BAD,zorder=3)
    lab=(f'option {V[(t,k)]:.4f}' if t<2 else f'payoff {V[(t,k)]:.1f}')
    ax.annotate(f'X = {x:.1f}\n{lab}',xy=(t,x),xytext=((7,-4) if t else (-6,22)),textcoords='offset points',fontsize=7.3,color=INK,va='center')
ax.set_xticks([0,1,2]);ax.set_xticklabels(['today','year 1','year 2'])
ax.set_xlim(-.15,2.75);ax.set_ylim(4,22);ax.set_ylabel('Project value X (USD M)')
ax.set_title('Two-year project: value and option value at every node',loc='left');ax.grid(alpha=.2)
