from matplotlib.patches import FancyBboxPatch
ax.set_xlim(9.3,16.2);ax.set_ylim(0,1);ax.axis('off');ax.hlines(.48,9.5,16,color=INK,lw=2)
for x,label,col in [(9.5,'Open',ACCENT),(10,'Decision',BAD),(12,'Noon',MUTED),(16,'Close',GOOD)]:
    ax.scatter(x,.48,s=45,color=col,zorder=3);ax.text(x,.34,label,ha='center',color=col,fontsize=8)
ax.axvspan(9.5,10,color=GOOD,alpha=.12);ax.axvspan(10,16,color=BAD,alpha=.08);ax.axvline(10,color=BAD,ls='--',lw=1.3)
ax.text(9.75,.72,'valid features',ha='center',color=GOOD,weight='bold');ax.text(13,.72,'future information',ha='center',color=BAD,weight='bold');ax.set_title('Decision-time filtration audit',loc='left')
