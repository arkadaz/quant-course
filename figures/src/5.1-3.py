labels=['Initial beta','QQQ reduction','SPY reduction','Residual beta']
vals=[1.10,0.40,0.50,0.20]
ax.bar(labels,vals,color=[ACCENT,WARM,GOOD,BAD],width=.58)
for i,v in enumerate(vals):ax.text(i,v+.035,f'{v:.2f}',ha='center',fontsize=9)
ax.set_ylim(0,1.25);ax.set_ylabel('Market beta')
ax.set_title('1.10 - 0.40 - 0.50 = 0.20',loc='left')
