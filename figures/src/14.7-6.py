
T=np.linspace(.03,4,300);v0=.09;th=.04
for k,c in zip([.5,2.,6.],[WARM,ACCENT,MUTED]):
 av=th+(v0-th)*(1-np.exp(-k*T))/(k*T);ax.plot(T,100*np.sqrt(av),color=c,label=f'kappa={k:.1f}')
ax.set_xlabel('Maturity (years)');ax.set_ylabel('Root expected average variance (%)');ax.legend()
