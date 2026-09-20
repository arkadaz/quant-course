labels=['Original cap USD 6M','Relaxed cap USD 7M'];vals=[1260,1200]
ax.bar(labels,vals,color=[ACCENT,GOOD],width=.52)
for i,v in enumerate(vals):ax.text(i,v+28,f'USD {v:,}',ha='center',fontsize=10,weight='bold')
ax.annotate('-USD 60',xy=(1,1200),xytext=(.55,1340),arrowprops=dict(arrowstyle='->',color=BAD),color=BAD,fontsize=10,weight='bold')
ax.set_ylim(0,1450);ax.set_ylabel('Optimal execution cost (USD)')
ax.set_title('The SPY-cap multiplier predicts the local cost saving',loc='left')
