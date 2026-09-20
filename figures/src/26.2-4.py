sr_perp=np.sqrt(500)*0.020/0.35
x=np.linspace(0,2.0,300)
ax.plot(x,np.sqrt(sr_perp**2+x**2),color=ACCENT,lw=2.4,label='combined Sharpe Ratio')
ax.axhline(sr_perp,color=MUTED,ls=':',lw=1.4)
ax.annotate(f'alpha orthogonal alone: {sr_perp:.3f}',xy=(1.35,sr_perp),xytext=(0,-14),
            textcoords='offset points',fontsize=7.5,color=MUTED)
ax.plot(0.375,np.sqrt(sr_perp**2+0.375**2),'o',color=WARM,ms=8)
ax.annotate(f'momentum at 0.375\nlifts it only to {np.sqrt(sr_perp**2+0.375**2):.3f} (+4.2%)',
            xy=(0.375,np.sqrt(sr_perp**2+0.375**2)),xytext=(0.52,1.32),fontsize=8,color=WARM,
            arrowprops=dict(arrowstyle='->',color=WARM,lw=.9))
ax.plot(1.278,np.sqrt(2)*sr_perp,'o',color=GOOD,ms=8)
ax.annotate('you need a factor bet as good as\nthe whole book to add 41%',
            xy=(1.278,np.sqrt(2)*sr_perp),xytext=(0.62,1.95),fontsize=8,color=GOOD,
            arrowprops=dict(arrowstyle='->',color=GOOD,lw=.9))
ax.set_xlabel('Sharpe Ratio of the factor bet you add')
ax.set_ylabel('Sharpe Ratio of the whole book')
ax.set_ylim(1.20,2.45)
ax.set_title('Adding in quadrature punishes the smaller source hard',loc='left')
ax.legend(fontsize=7,loc='upper left')
