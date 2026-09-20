v=np.array([40_000.,70_000.,50_000.,120_000.])
C=np.array([[1,.25,.45,0],[.25,1,-.15,0],[.45,-.15,1,0],[0,0,0,1]])
Om=np.outer(v,v)*C;vtot=np.sqrt(Om.sum())
m=Om.sum(axis=1)/(v*vtot)
sr=np.array([0.0,0.8,0.0,1.6]);d=np.sqrt(251)
srtot=(sr/d*v).sum()/vtot*d
sens=srtot/vtot*(sr/srtot-m)*1e5
x=np.arange(4)
ax.bar(x-0.19,sr/srtot,width=.36,color=ACCENT,label='what it pays: SR of the group over SR of the book')
ax.bar(x+0.19,m,width=.36,color=GRID,edgecolor=MUTED,label='what it costs: MCR')
for i in range(4):
    good=sens[i]>0
    ax.annotate(f'{sens[i]:+.3f}',xy=(i,max(sr[i]/srtot,m[i])),xytext=(0,9),textcoords='offset points',
                fontsize=9,ha='center',color=GOOD if good else BAD,weight='bold')
    ax.annotate('grow' if good else 'shrink',xy=(i,max(sr[i]/srtot,m[i])),xytext=(0,25),
                textcoords='offset points',fontsize=7.5,ha='center',color=GOOD if good else BAD)
ax.set_xticks(x);ax.set_xticklabels(['market','style','industry','idio'])
ax.set_ylabel('ratio (unitless)')
ax.set_ylim(0,1.42)
ax.set_title('Numbers above the bars: change in annual Sharpe per 100k USD of daily volatility',
             loc='left',fontsize=9)
ax.legend(fontsize=7,loc='upper left')
