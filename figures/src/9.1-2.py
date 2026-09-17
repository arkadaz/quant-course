x=[0,1,1];y=[570,576,564]
ax.plot([0,1],[570,576],color=GOOD,lw=2);ax.plot([0,1],[570,564],color=BAD,lw=2)
ax.scatter(x,y,c=[INK,GOOD,BAD],s=38,zorder=3)
ax.axhline(570,color=ACCENT,ls='--',label='conditional mean = current')
ax.text(1.02,576,'USD 576, p=0.50',va='center');ax.text(1.02,564,'USD 564, p=0.50',va='center')
ax.set_xlim(-0.08,1.55);ax.set_xticks([0,1],['Now','Tomorrow']);ax.set_ylabel('SPY price (USD)');ax.legend(loc='upper left')
