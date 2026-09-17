labels=['QQQ','SPY'];vals=[180/1.2,90/1.0]
ax.bar(labels,vals,color=[WARM,GOOD],width=.5)
for i,v in enumerate(vals):ax.text(i,v+5,f'USD {v:.0f}',ha='center',fontsize=10,weight='bold')
ax.set_ylim(0,175);ax.set_ylabel('Cost per beta-USD million removed (USD)')
ax.set_title('Cheaper beta reduction uses SPY capacity first',loc='left')
