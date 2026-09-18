x=np.linspace(0,.2,300)
for p0,c in [(.52,BAD),(.55,ACCENT)]:
    ax.plot(x*100,100*(p0*np.log1p(x)+(1-p0)*np.log1p(-x)),color=c,lw=1.8,label=f'true p = {p0:.0%}, peak at {100*(2*p0-1):.0f}%')
ax.axvline(10,color=INK,ls=':',lw=1);ax.text(10.3,.42,'size chosen from p = 55%',fontsize=7.3)
g52=.52*np.log1p(.1)+.48*np.log1p(-.1);ax.scatter([10],[100*g52],color=BAD,zorder=3)
ax.annotate(f'{100*g52:+.3f}% per round',(10,100*g52),xytext=(12,-.25),fontsize=7.3,arrowprops=dict(arrowstyle='->',lw=.8))
ax.axhline(0,color=MUTED,lw=.9);ax.set_xlabel('Fraction at risk (%)');ax.set_ylabel('Log growth (% per round)')
ax.set_title('Three points of overconfidence put you past the zero line',loc='left');ax.legend(fontsize=7.3,loc='lower left');ax.grid(alpha=.2)
