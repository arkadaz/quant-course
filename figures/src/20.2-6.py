lp1=[1,0.773,0.691,0.500,0.361];lp2=[1,0.694,0.540,0.346,0.293]
sp1=[1,0.98,0.92,0.86,0.79,0.72,0.64];sp2=[1,0.99,0.94,0.90,0.86,0.82,0.75]
ax.plot(range(1,8),sp1,'s-',color=ACCENT,lw=1.6,ms=5,label='Swaps, Jan 2014 to May 2016')
ax.plot(range(1,8),sp2,'s--',color=ACCENT,lw=1.6,ms=5,alpha=.7,label='Swaps, May 2016 to Oct 2018')
ax.plot(range(1,6),lp1,'o-',color=WARM,lw=1.6,ms=5,label='LIBOR, Jan 2014 to May 2016')
ax.plot(range(1,6),lp2,'o--',color=WARM,lw=1.6,ms=5,alpha=.7,label='LIBOR, May 2016 to Oct 2018')
ax.set_xticks(range(1,8));ax.set_xlabel('Maturity rank (1 = shortest in each set)')
ax.set_ylabel('Correlation with the shortest maturity');ax.set_ylim(0.2,1.03)
ax.set_title('Swap rates move together; LIBOR tenors drift apart',loc='left');ax.legend(fontsize=7,loc='lower left');ax.grid(alpha=.2)
