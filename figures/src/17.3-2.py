w=np.linspace(-.2,1.2,400);sd=np.sqrt(.04*w*w+.0036*(1-w)**2+2*.0018*w*(1-w));m=.035+.055*w
wt=0.321888;st=np.sqrt(.04*wt**2+.0036*(1-wt)**2+2*.0018*wt*(1-wt));mt=.035+.055*wt
ax.plot(sd*100,m*100,label='Risky-asset frontier');s=np.linspace(0,.25,100);ax.plot(s*100,(.02+s*(mt-.02)/st)*100,label='Cash + tangency');ax.scatter([st*100],[mt*100],color=BAD);ax.set_xlabel('One-year standard deviation (%)');ax.set_ylabel('Expected one-year return (%)');ax.legend(fontsize=7)
