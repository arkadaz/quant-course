
k=np.linspace(-.28,.24,240)
for T,c in zip([.08,.25,1.0],[WARM,ACCENT,MUTED]):
 iv=.20+.06*np.exp(-2*T)-.12*k+.15*k*k;ax.plot(k,100*iv,color=c,label=f'{T:.2f}y')
ax.set_xlabel('Log-moneyness log(K/F)');ax.set_ylabel('Implied volatility (%)');ax.legend(title='Maturity')
