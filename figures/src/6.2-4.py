fig=ax.figure
ax.remove()
ax=fig.add_subplot(111,projection='3d')
vecs=[(1,0,1,ACCENT,'u'),(0,1,1,WARM,'v'),(1,1,0,GOOD,'w')]
for x,y,z,c,label in vecs:
 ax.quiver(0,0,0,x,y,z,color=c,arrow_length_ratio=.10,linewidth=2)
 ax.text(x*1.08,y*1.08,z*1.08,label,color=c,fontsize=10)
ax.set_xlim(0,1.35);ax.set_ylim(0,1.35);ax.set_zlim(0,1.35)
ax.set_xlabel('factor 1');ax.set_ylabel('factor 2');ax.set_zlabel('factor 3')
ax.set_title(r'Independent vectors span $\mathbb{R}^3$',loc='left')
