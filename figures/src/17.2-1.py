x=np.linspace(0,.42,400);g=lambda f:.55*np.log1p(f)+.45*np.log1p(-f)
ax.plot(100*x,100*g(x),color=ACCENT,lw=1.8)
pts=np.array([.05,.10,.15,.20,.40])
ax.scatter(100*pts,100*g(pts),color=BAD,zorder=3)
for f in pts:
    ax.annotate(f'{100*g(f):+.3f}%',(100*f,100*g(f)),xytext=(4,6 if f<.3 else -12),textcoords='offset points',fontsize=7.3)
ax.axhline(0,color=MUTED,lw=.9);ax.axvline(19.87,color=MUTED,ls=':',lw=1);ax.text(20.4,-1.2,'zero at 19.87%',fontsize=7.3)
ax.set_xlabel('Fraction of wealth at risk f (%)');ax.set_ylabel('Log growth g(f) (% per round)')
ax.set_title('p = 55%, 1:1 payoff: the peak is at 10%, the cliff past 20%',loc='left');ax.grid(alpha=.2)
