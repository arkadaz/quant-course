w=np.linspace(0,1,301);q=.038*w**2-.008*w+.01;wm=.008/.076
ax.plot(w*100,np.sqrt(q)*100,color=ACCENT,lw=2);ax.scatter([wm*100],[np.sqrt(.009578947)*100],color=GOOD,s=50,label='minimum variance');ax.set_xlabel('SPY weight (%)');ax.set_ylabel('Annual volatility (%)');ax.legend();ax.set_title('Full investment removes the zero portfolio',loc='left')
