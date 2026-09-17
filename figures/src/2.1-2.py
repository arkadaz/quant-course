labels=['Normal contribution','Event-stress contribution']
values=[0.80*100,0.20*(-600)]
colors_=[GOOD,BAD]
ax.bar(labels,values,color=colors_)
ax.axhline(0,color=MUTED,lw=0.8)
for i,v in enumerate(values): ax.text(i,v+(12 if v>=0 else -18),f'{v:+.0f} USD/day',ha='center',va='bottom' if v>=0 else 'top',fontsize=8)
ax.set_ylabel('probability-weighted P&L (USD/day)')
ax.set_title('Outer expectation adds weighted regime contributions',fontsize=9,loc='left')
