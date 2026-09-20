labels=['Success','Ladder failure'];probs=np.array([511/512,1/512]);pnl=np.array([1000,-511000]);weighted=probs*pnl
x=np.arange(2);ax.bar(x,weighted,color=[GOOD,BAD],width=0.55);ax.axhline(0,color=INK,lw=0.8)
ax.set_xticks(x,labels);ax.set_ylabel('Probability-weighted P&L (USD)')
for i,v in enumerate(weighted):ax.text(i,v+(35 if v>=0 else -35),f'{v:+,.2f}',ha='center',va='bottom' if v>=0 else 'top')
ax.set_title('99.8047% success still nets to zero expectation',fontsize=9,loc='left')
ax.set_ylim(-1200,1200)
