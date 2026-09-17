shapes=['A: 3×2','Aᵀ: 2×3','w: 3×1']
vals=[3,2,3]
ax.bar(shapes,vals,color=[ACCENT,WARM,GOOD])
ax.set_ylabel('row count')
ax.set_title('Shape metadata is part of the risk contract',fontsize=9,loc='left')
