d=np.linspace(0,.8,161);rec=d/(1-d)
ax.plot(100*d,100*rec,color=ACCENT,lw=2);ax.scatter([10,20,50],[100*10/90,25,100],color=BAD);ax.set_xlabel('Drawdown from peak (%)');ax.set_ylabel('Required return to recover (%)');ax.grid(alpha=.25)
