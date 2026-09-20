x=np.linspace(0,10,200); y=(10-x)/2
ax.plot(x,y,color=BAD,lw=2)
ax.fill_between(x,0,y,color=GOOD,alpha=0.18)
ax.scatter([4,8],[2,3],s=45,color=[GOOD,BAD])
ax.annotate('feasible (4,2)',(4,2),xytext=(4.5,2.7),fontsize=8)
ax.annotate('reject (8,3)',(8,3),xytext=(8.1,3.6),fontsize=8)
ax.set_xlim(-0.5,10.8);ax.set_ylim(-0.3,5.8);ax.set_xlabel('x1 (USD million)');ax.set_ylabel('x2 (USD million)')
ax.set_title('Feasibility is checked before optimization',fontsize=9,loc='left')
