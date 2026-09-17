q=np.linspace(.001,1,500);ax.plot(12*q,np.sqrt(q),color=ACCENT,lw=2,label='correlation')
ax.plot(12*q,q,color=GOOD,lw=2,label='$R^2$')
ax.scatter([1,1],[np.sqrt(1/12),1/12],color=[ACCENT,GOOD],s=40,zorder=4);ax.axvline(1,color=MUTED,ls='--',lw=1)
ax.set_xlabel('Months observed');ax.set_ylabel('Relationship to full-year total');ax.set_ylim(0,1.05);ax.set_title('Overlap creates correlation without prediction',loc='left');ax.legend(loc='lower right')
