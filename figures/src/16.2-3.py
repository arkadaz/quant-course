phi=.88;h=np.arange(0,25);dev=30*phi**h;hl=np.log(.5)/np.log(phi)
ax.plot(h,dev,color=ACCENT,lw=2,marker='o',ms=3,label='expected distance from 15 bp')
ax.axhline(15,color=WARM,ls='--',label='half of the 30 bp start')
ax.axvline(hl,color=BAD,ls='--');ax.scatter([hl],[15],color=BAD,zorder=3)
for k,dx,dy in ((1,6,6),(5,-34,-14),(6,6,6)):
 ax.annotate(f'{dev[k]:.2f}',(k,dev[k]),textcoords='offset points',xytext=(dx,dy),fontsize=7)
ax.set_xlabel('forecast horizon (months)');ax.set_ylabel('distance from mean (bp)')
ax.set_title(f'Half-life = {hl:.2f} months: 15.83 at month 5, 13.93 at month 6',loc='left');ax.legend(fontsize=7)
