w=np.linspace(0,1,300);v=.04*w*w+.0036*(1-w)**2+2*.0018*w*(1-w)
ax.plot(w*100,np.sqrt(v)*100);ax.scatter([4.5],[np.sqrt(.003519)*100],color=BAD);ax.set_xlabel('Equity weight (%)');ax.set_ylabel('One-year standard deviation (%)')
