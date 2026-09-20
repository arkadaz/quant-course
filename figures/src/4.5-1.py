ax.axhline(0,color=MUTED,lw=.8);ax.axvline(0,color=MUTED,lw=.8)
vecs=[((1,-1),ACCENT,'x'),((1,0),GOOD,'acute: dot > 0'),((1,1),WARM,'orthogonal: dot = 0'),((-1,2),BAD,'obtuse: dot < 0')]
for (dx,dy),c,lbl in vecs: ax.quiver(0,0,dx,dy,angles='xy',scale_units='xy',scale=1,color=c,width=.009,label=lbl)
ax.set_aspect('equal');ax.set_xlim(-1.5,1.6);ax.set_ylim(-1.5,2.5)
ax.set_xlabel('centered return axis 1');ax.set_ylabel('centered return axis 2')
ax.legend(loc='upper left',fontsize=7);ax.set_title('Acute, right, and obtuse geometry',loc='left')
