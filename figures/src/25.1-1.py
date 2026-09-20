rf=np.linspace(0,.10,101)
A,rL,rS=200.,.110,.060
neutral=(300*rL-300*rS-0*rf)/A*100
netlong=(350*rL-250*rS-100*rf)/A*100
ax.plot(rf*100,neutral,color=ACCENT,lw=2.2,label='NMV = 0  (long 300M, short 300M)')
ax.plot(rf*100,netlong,color=WARM,lw=2.2,label='NMV = 100M USD (long 350M, short 250M)')
ax.axvline(4.8,color=MUTED,ls=':',lw=1.2)
ax.annotate('SOFR 4.8%',xy=(4.8,2.4),fontsize=7,color=MUTED,rotation=90,va='bottom',ha='right')
ax.annotate('7.50% at every rate',xy=(7.5,7.5),xytext=(5.9,9.4),fontsize=7.5,color=ACCENT,
            arrowprops=dict(arrowstyle='->',color=ACCENT,lw=.8))
ax.annotate('11.00% down to 8.50%\n0.5 pt lost per 1 pt of SOFR',xy=(4.8,8.5),xytext=(0.6,3.6),fontsize=7.5,color=WARM,
            arrowprops=dict(arrowstyle='->',color=WARM,lw=.8))
ax.set_xlabel('SOFR for the year (%)');ax.set_ylabel('return on 200M USD of capital (%)')
ax.set_ylim(2,12)
ax.set_title('A zero-NMV book does not care what the rate is',loc='left');ax.legend(fontsize=7,loc='lower left')
