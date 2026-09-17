x=np.linspace(-4,4,500)
for t,col in zip([1,4,9],[ACCENT,WARM,GOOD]): ax.plot(x,stats.norm.pdf(x,0,1),color=col,lw=2-(t-1)*.03,alpha=.88,label=fr'$W_{t}/\sqrt{{{t}}}$')
ax.fill_between(x,stats.norm.pdf(x),color=ACCENT,alpha=.07)
ax.set_xlabel('Scaled terminal value');ax.set_ylabel('Density');ax.set_title('All scaled horizons return to N(0,1)',loc='left');ax.legend(loc='upper right')
