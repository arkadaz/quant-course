x=np.linspace(4,22,300)
ax.plot(x,x-9,color=MUTED,lw=1.2,ls=(0,(4,3)),label='forced to invest: X - 9')
ax.plot(x,np.maximum(x-9,0),color=ACCENT,lw=2.4,label='right to invest: max(X - 9, 0)')
pts=[(6.4,0.0),(11.2,2.2),(19.6,10.6)]
ax.scatter([p[0] for p in pts],[p[1] for p in pts],color=INK,s=30,zorder=3)
for xx,yy in pts:
    ax.annotate(f'X = {xx}: {yy}',xy=(xx,yy),xytext=((-22,9) if yy==0 else (9,-13)),textcoords='offset points',fontsize=7.5)
ax.annotate('forced: -2.6',xy=(6.4,-2.6),xytext=(7,-3),textcoords='offset points',fontsize=7.5,color=MUTED)
ax.scatter([6.4],[-2.6],color=MUTED,s=22,zorder=3)
ax.axhline(0,color=INK,lw=.6)
ax.set_xlabel('Project value in year 2, X (USD M)');ax.set_ylabel('Payoff (USD M)')
ax.set_title('The right to walk away turns -2.6 into 0',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(alpha=.2)
