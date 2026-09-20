x=np.linspace(0,12,300);ax.plot(x,2*np.log1p(x),color=ACCENT,lw=2,label='Desk 1');ax.plot(x,4*np.log1p(x),color=GOOD,lw=2,label='Desk 2')
ax.set_xlabel('Allocated capital (USD million)');ax.set_ylabel('Expected annual profit (USD million)');ax.legend();ax.set_title('Capacity makes marginal profit decline',loc='left')
