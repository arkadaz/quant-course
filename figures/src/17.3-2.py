w=np.linspace(-.4,1.3,400);sd=np.sqrt(.04*w*w+.01*(1-w)**2+.008*w*(1-w));m=.04+.04*w
wt=13/27;st=np.sqrt(.04*wt**2+.01*(1-wt)**2+.008*wt*(1-wt));mt=.04+.04*wt
ax.plot(sd*100,m*100,label='Risky-asset frontier');s=np.linspace(0,.27,100);ax.plot(s*100,(.02+s*(mt-.02)/st)*100,label='Cash + tangency');ax.scatter([st*100],[mt*100],color=BAD);ax.set_xlabel('One-year standard deviation (%)');ax.set_ylabel('Expected one-year return (%)');ax.legend(fontsize=7)
