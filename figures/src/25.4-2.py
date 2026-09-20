se,sn,M=0.0256,0.012,390
q=np.arange(1,121)
m=M/q
bias=2*m*sn**2
var=2*m*(q*se**2)**2
tot=np.sqrt(bias**2+var)
true=M*se**2
ax.loglog(q,bias/true*100,color=BAD,lw=2.0,ls='--',label='bias from microstructure noise')
ax.loglog(q,np.sqrt(var)/true*100,color=GOOD,lw=2.0,ls='--',label='random error from fewer points')
ax.loglog(q,tot/true*100,color=ACCENT,lw=2.6,label='total error (root mean squared)')
qs=int(q[np.argmin(tot)])
ax.plot(qs,tot[qs-1]/true*100,'o',color=INK,ms=8)
ax.annotate(f'lowest at {qs} minutes\n({tot[qs-1]/true*100:.1f}% of the daily variance)',
            xy=(qs,tot[qs-1]/true*100),xytext=(7,26),fontsize=8,color=INK,
            arrowprops=dict(arrowstyle='->',color=INK,lw=.9))
ax.axvspan(3,10,color=GRID,alpha=.6,zorder=0)
ax.annotate('3 to 10 minutes all within 10%',xy=(5.5,7.0),fontsize=7,color=MUTED,ha='center')
ax.set_xlabel('minutes per sampled interval');ax.set_ylabel('error as % of the daily variance')
ax.set_title('Sample too often and bias wins; too rarely and noise wins',loc='left')
ax.legend(fontsize=7,loc='upper right')
