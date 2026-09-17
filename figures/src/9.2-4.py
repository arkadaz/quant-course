x=np.linspace(-3.5,3.5,500);y=stats.norm.pdf(x);ax.plot(x,y,color=ACCENT);mask=x>=0.74;ax.fill_between(x[mask],0,y[mask],color=WARM,alpha=0.45,label='one-sided tail = 22.96%')
ax.axvline(0.74,color=BAD,ls='--');ax.text(0.82,0.30,'observed z = 0.74',color=BAD)
ax.set_xlabel('z-score');ax.set_ylabel('Density');ax.legend(loc='upper left')
