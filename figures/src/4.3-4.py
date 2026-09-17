labels=['A columns','w rows','output rows']
vals=[3,3,3]
ax.bar(labels,vals,color=[ACCENT,GOOD,WARM])
ax.set_ylim(0,4);ax.set_ylabel('dimension count')
ax.set_title('Matching inner dimensions makes Aw legal',fontsize=9,loc='left')
