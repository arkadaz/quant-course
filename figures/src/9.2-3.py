n=np.arange(1,253);nav=25e6;sd=nav*.0115*np.sqrt(n);wrong=nav*.0115*n
ax.plot(n,sd/1e6,color=ACCENT,lw=2,label='correct: square-root-of-time')
ax.plot(n,wrong/1e6,color=BAD,lw=1.5,ls='--',label='wrong: linear volatility')
for k in [1,5,21,252]:ax.scatter(k,nav*.0115*np.sqrt(k)/1e6,color=GOOD,s=30,zorder=4)
ax.set_xlabel('Trading days');ax.set_ylabel('One-SD P&L (USD million)');ax.set_yscale('log');ax.set_title('Volatility does not add across days',loc='left');ax.legend(loc='upper left')
