a=np.linspace(0,1,201);var=.04*a**2+.012*a*(1-a)+.01*(1-a)**2;chord=a*.04+(1-a)*.01
ax.plot(a,var,color=ACCENT,lw=2,label='portfolio variance');ax.plot(a,chord,color=WARM,ls='--',label='chord');ax.fill_between(a,var,chord,color=GOOD,alpha=.18);ax.set_xlabel('SPY weight');ax.set_ylabel('Annual variance');ax.legend();ax.set_title('A convex risk curve stays below every chord',loc='left')
