labels=['inner product','divide by norms','correlation']
vals=[1,.5,.5]
ax.bar(labels,vals,color=[ACCENT,WARM,GOOD],width=.55)
for i,v in enumerate(vals): ax.text(i,v+.05,f'{v:g}',ha='center',fontsize=11,color=INK)
ax.annotate('',xy=(.85,.55),xytext=(.35,.55),arrowprops=dict(arrowstyle='->',color=MUTED))
ax.annotate('',xy=(1.85,.55),xytext=(1.35,.55),arrowprops=dict(arrowstyle='->',color=MUTED))
ax.set_ylim(0,1.25);ax.set_ylabel('value after each operation')
ax.set_title('Dot product to angle to correlation',loc='left')
