labels=['Net exposure','Gross exposure']
vals=[15,25]
ax.bar(labels,vals,color=[ACCENT,WARM],width=0.48)
for i,v in enumerate(vals): ax.text(i,v+0.8,f'${v}M',ha='center',fontsize=10,color=INK,weight='bold')
ax.set_ylim(0,30)
ax.set_ylabel('Exposure ($M)')
ax.set_title('Signed risk and deployed capital are not the same number',loc='left')
