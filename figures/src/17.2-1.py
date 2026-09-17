x=np.linspace(0,.4,400);g=lambda f:.55*np.log1p(f)+.45*np.log1p(-f)
ax.plot(100*x,100*g(x));ax.scatter([5,10,20],100*g(np.array([.05,.1,.2])),color=BAD);ax.axhline(0,color=MUTED);ax.set_xlabel('Fraction of wealth at risk (%)');ax.set_ylabel('Expected log growth (% per round)')
