x=np.linspace(-.16,.22,500); mu=.03; sig=.06
for n,c in zip([1,4,16],SERIES[:3]):
 s=sig/np.sqrt(n); ax.plot(x,stats.norm.pdf(x,mu,s),color=c,lw=2,label=f'n={n}, SE={100*s:.1f}%')
ax.axvline(mu,color=INK,lw=1,ls='--'); ax.set(xlabel='Annual active return',ylabel='Density'); ax.legend(fontsize=7); ax.grid(alpha=.2)
