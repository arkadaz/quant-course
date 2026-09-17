labels=['Technology','Energy','Financials']
mu=np.array([0.0005,0.0002,0.00035])*10000
ax.bar(labels,mu,color=[ACCENT,WARM,GOOD])
ax.axhline(0,color=MUTED,lw=0.8)
for i,v in enumerate(mu): ax.text(i,v+0.05,f'{v:.1f}',ha='center',fontsize=8)
ax.set_ylabel('mean daily return (basis points)')
ax.set_title('Mean vector: one centre per sector return',fontsize=9,loc='left')
