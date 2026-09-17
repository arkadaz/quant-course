w=np.linspace(0,1,300);v=.04*w*w+.01*(1-w)**2+.008*w*(1-w)
ax.plot(w*100,np.sqrt(v)*100);ax.scatter([100/7],[np.sqrt(.009142857142857)*100],color=BAD);ax.set_xlabel('Equity weight (%)');ax.set_ylabel('One-year standard deviation (%)')
