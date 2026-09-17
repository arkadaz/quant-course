pts=[(0,1),(2,1),(4,1),(4,0),(2,0),(0,0)];labs=['Housing/credit\nloss','MBS/CDO\nmark down','Higher repo\nhaircut','Forced\nsale','Lower market\nliquidity','Wider marks'];nodes=[];
for i,(x,y) in enumerate(pts): nodes.append(ax.text(x,y,labs[i],ha='center',va='center',fontsize=8,bbox=dict(boxstyle='round',fc='#F6F8FA',ec=ACCENT),zorder=3));
for i,(x,y) in enumerate(pts): ax.annotate('',xy=pts[(i+1)%6],xytext=(x,y),arrowprops=dict(arrowstyle='->',color=BAD,lw=1.5,patchA=nodes[i].get_bbox_patch(),patchB=nodes[(i+1)%6].get_bbox_patch(),shrinkA=2,shrinkB=2),zorder=2);
ax.set_xlim(-.8,4.8);ax.set_ylim(-.6,1.6);ax.axis('off');ax.set_title('Loss, funding and liquidity reinforce one another',loc='left')
