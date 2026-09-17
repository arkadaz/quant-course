
k=np.linspace(-.30,.25,260);iv=.20-.11*k+.16*k*k
ax.plot(k,100*iv,color=ACCENT);ax.axvline(0,color=MUTED,ls='--',label='At-forward')
ax.set_xlabel('Log-moneyness log(K/F)');ax.set_ylabel('Implied volatility (%)');ax.legend()
