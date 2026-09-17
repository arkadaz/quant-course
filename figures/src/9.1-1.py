from matplotlib.patches import Rectangle
ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis('off')
boxes=[(0.7,1.9,2.1,2.0,'F0','Open'),(0.7,1.2,4.2,3.4,'F1','Price + news'),(0.7,0.5,6.4,4.8,'F2','Price + news + flow')]
for i,(x,y,w,h,f,label) in enumerate(boxes):
    ax.add_patch(Rectangle((x,y),w,h,fill=False,lw=2,color=SERIES[i]))
    ax.text(x+w-0.15,y+h-0.32,f'{f}: {label}',ha='right',va='top',color=SERIES[i],fontsize=8)
ax.axvline(7.8,color=BAD,ls='--',lw=1.5);ax.text(7.95,4.9,'Future price\nnot observable yet',color=BAD,va='top')
ax.annotate('information only grows',xy=(6.8,0.7),xytext=(3.8,0.1),arrowprops=dict(arrowstyle='->',color=INK),ha='center')
