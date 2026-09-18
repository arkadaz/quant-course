q=np.linspace(0,1,401);imp=0.8*1.8*np.sqrt(q)*100
ax.plot(100*q,imp,color=ACCENT,lw=2.2,label='impact = 0.8 x 1.8% x sqrt(Q/V)')
ax.plot(100*q,144*q,color=MUTED,lw=1.2,ls=(0,(4,3)),label='if impact were linear')
pts=[(5,32.2,'Q 40M: 32.2 bp'),(25,72.0,'Q 200M: 72 bp'),(100,144.0,'Q 800M: 144 bp')]
for x,y,t in pts:
    ax.scatter([x],[y],color=INK,zorder=3,s=26);ax.annotate(t,xy=(x,y),xytext=(6,-12),textcoords='offset points',fontsize=7.5)
ax.set_xlabel('Order as % of daily volume, Q/V');ax.set_ylabel('Price impact (bp)')
ax.set_title('Square-root law: 4x the size, 2x the impact per share',loc='left');ax.legend(fontsize=7.5,loc='upper left');ax.grid(alpha=.2)
