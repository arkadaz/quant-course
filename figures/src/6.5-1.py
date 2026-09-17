labels=['Mean sum','Product mean','Variance sum']
ind=[1.0,1.0,1.0]
need=['always','needs X⊥Y','needs X⊥Y']
ax.bar(labels,ind,color=[GOOD,ACCENT,WARM])
for i,t in enumerate(need): ax.text(i,0.5,t,ha='center',color='white',weight='bold')
ax.set_ylim(0,1.2);ax.set_ylabel('validity indicator')
ax.set_title('Independence is a condition, not a universal shortcut',fontsize=9,loc='left')
