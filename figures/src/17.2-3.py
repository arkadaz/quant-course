x=np.linspace(0,.2,300)
for p0,c in [(.51,BAD),(.55,ACCENT),(.59,GOOD)]:ax.plot(x*100,100*(p0*np.log1p(x)+(1-p0)*np.log1p(-x)),color=c,label=f'p={p0:.0%}')
ax.axhline(0,color=MUTED);ax.set_xlabel('Fraction at risk (%)');ax.set_ylabel('Expected log growth (% per round)');ax.legend()
