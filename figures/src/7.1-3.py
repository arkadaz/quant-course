ax.barh(['AAPL','MSFT','JPM'],[2,-1,0.5],color=[GOOD,BAD,ACCENT])
ax.axvline(0,color=MUTED,lw=0.8)
ax.set_xlabel('position w (USD million)')
ax.set_title('One USD million position value per matrix row',fontsize=9,loc='left')
