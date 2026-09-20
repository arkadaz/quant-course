
T=np.linspace(.02,5,300);th=.04;k=2
for v0,c in zip([.04,.09,.16],[MUTED,ACCENT,WARM]):
 av=th+(v0-th)*(1-np.exp(-k*T))/(k*T);ax.plot(T,100*np.sqrt(av),color=c,label=f'sqrt(v0)={100*np.sqrt(v0):.0f}%')
ax.axhline(20,color=GOOD,ls='--',label='Long-run 20%');ax.set_xlabel('Maturity (years)');ax.set_ylabel('Root expected average variance (%)');ax.legend()
