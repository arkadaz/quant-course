x=np.linspace(-8,8,320)
for mean,scale,col,label in [(0.04,2.0,ACCENT,'SPX marginal'),(0.03,3.0,WARM,'QQQ marginal')]:
    z=stats.norm.pdf(x,loc=mean,scale=scale);ax.plot(x,z,color=col,lw=2,label=label)
ax.set_xlabel('daily return (%)');ax.set_ylabel('density');ax.legend(loc='upper left')
ax.set_title('A selection matrix chooses one marginal at a time',fontsize=9,loc='left')
