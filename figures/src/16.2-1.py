rng=np.random.default_rng(1602);e=rng.normal(0,1,90);t=np.arange(90);ax.axhline(0,color=INK,lw=.7);cols=[ACCENT,WARM,BAD];phis=[.2,.9,1.0];
for phi,c in zip(phis,cols):
 x=np.zeros(90)
 for i in range(1,90): x[i]=phi*x[i-1]+e[i]
 ax.plot(t,x,label=f'phi={phi}',color=c)
ax.set_xlabel('month');ax.set_ylabel('distance from mean (shock units)');ax.set_title('Persistence is visible before it is estimated',loc='left');ax.legend(fontsize=7)
