
stock=36.7718655;cash=-34.3809885;net=stock+cash
ax.bar(['Stock leg','Cash account'],[stock,cash],color=[ACCENT,BAD]);ax.axhline(0,color=INK,lw=1)
ax.scatter([1.5],[net],s=70,color=GOOD,label=f'Net call = {net:.4f} USD')
ax.set_ylabel('Value (USD)');ax.set_xlim(-.6,2.0);ax.legend()
