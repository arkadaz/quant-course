n=np.linspace(1,70,300)
for ir,c in zip([.25,.5,1.0],SERIES[:3]): ax.plot(n,ir*np.sqrt(n),color=c,lw=2,label=f'IR={ir:.2f}')
ax.axhline(2,color=BAD,lw=1.2,ls='--',label='t=2'); ax.set(xlabel='Independent years',ylabel='Expected t-statistic',ylim=(0,8.6)); ax.legend(fontsize=7); ax.grid(alpha=.25)
