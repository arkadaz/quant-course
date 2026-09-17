U=np.linspace(3.6,8.0,160);cost=1620-60*U
ax.plot(U,cost,color=ACCENT,lw=2)
ax.scatter([6,7],[1260,1200],color=[BAD,GOOD],s=48,zorder=4)
ax.annotate('USD 1M more capacity\nsaves USD 60',xy=(7,1200),xytext=(6.55,1370),arrowprops=dict(arrowstyle='->',color=MUTED),fontsize=8)
ax.set_xlabel('SPY capacity, $U_S$ (USD million)');ax.set_ylabel('Optimal cost (USD)')
ax.set_title('Local slope = -USD 60 per additional USD 1M of SPY capacity',loc='left')
