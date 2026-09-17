x=np.linspace(-7,7,700)
for s,col in zip([.25,1,4],[WARM,ACCENT,GOOD]):
    ax.plot(x,stats.norm.pdf(x,0,np.sqrt(s)),color=col,label=f'horizon={s:g}, SD={np.sqrt(s):g}')
ax.set_xlabel('Increment');ax.set_ylabel('Density');ax.set_title(r'Normal increments widen with $\sqrt{s}$',loc='left');ax.legend(loc='upper right')
