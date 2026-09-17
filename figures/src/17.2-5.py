p=np.linspace(.45,.65,300);f=np.maximum(0,2*p-1)
ax.plot(100*p,100*f,color=ACCENT,lw=2);ax.scatter([51,55],[2,10],color=[BAD,WARM]);ax.axvline(50,color=MUTED,ls='--');ax.set_xlabel('Assumed win probability (%)');ax.set_ylabel('Full-Kelly fraction at risk (%)');ax.grid(alpha=.25)
