sr=np.linspace(0.2,3.0,300)
yrs=(2/sr)**2
ax.semilogy(sr,yrs,color=ACCENT,lw=2.4)
for s,lab in [(0.5,'16 years'),(1.0,'4 years'),(2.0,'1 year')]:
    ax.plot(s,(2/s)**2,'o',color=WARM,ms=7)
    ax.annotate(f'SR {s:.1f}\n{lab}',xy=(s,(2/s)**2),xytext=(10,8),textcoords='offset points',fontsize=8,color=WARM)
ax.axhline(1,color=GRID,lw=1)
ax.annotate('this curve does not move\nwhen you buy faster data',xy=(2.3,20),fontsize=8,color=MUTED)
ax.set_xlabel('annualised Sharpe Ratio');ax.set_ylabel('years to reach t = 2')
ax.set_title('Proving a strategy works is a question of time, not of data',loc='left')
