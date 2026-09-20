ax.axis('off')
import matplotlib.patches as mp
ax.add_patch(mp.Polygon([[0.05,0.22],[0.78,0.10],[0.95,0.34],[0.22,0.46]],
                        closed=True,facecolor=GRID,edgecolor=MUTED,lw=1.2,alpha=.85,zorder=1))
ax.text(0.50,0.17,'everything the old model can already say',ha='center',fontsize=8,color=MUTED,zorder=4)
ax.annotate('',xy=(0.70,0.82),xytext=(0.30,0.28),arrowprops=dict(arrowstyle='->',color=INK,lw=2.4),zorder=5)
ax.annotate('',xy=(0.70,0.30),xytext=(0.30,0.28),arrowprops=dict(arrowstyle='->',color=ACCENT,lw=2.4),zorder=5)
ax.annotate('',xy=(0.70,0.82),xytext=(0.70,0.30),arrowprops=dict(arrowstyle='->',color=WARM,lw=2.6),zorder=5)
ax.plot([0.655,0.655,0.70],[0.30,0.345,0.345],color=MUTED,lw=1.1,zorder=5)
ax.text(0.44,0.62,'the raw new characteristic',fontsize=9,color=INK,rotation=40)
ax.text(0.40,0.245,'the part already in the model',fontsize=8.5,color=ACCENT)
ax.text(0.725,0.55,'what is genuinely new\n(this is what you regress)',fontsize=8.5,color=WARM)
ax.set_xlim(0,1.08);ax.set_ylim(0.03,0.95)
ax.set_title('The middle step you are not allowed to skip',loc='left')
