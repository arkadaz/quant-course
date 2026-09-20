v=np.array([40_000.,70_000.,50_000.,120_000.])
C=np.array([[1,.25,.45,0],[.25,1,-.15,0],[.45,-.15,1,0],[0,0,0,1]])
Om=np.outer(v,v)*C;vtot=np.sqrt(Om.sum())
p=Om.sum(axis=1)/vtot**2;m=Om.sum(axis=1)/(v*vtot)
names=['market','style','industry','idio']
cols=[BAD,WARM,BAD,GOOD]
ax.scatter(p*100,m,s=v/260,c=cols,alpha=.85,zorder=3)
for i,n in enumerate(names):
    ax.annotate(f'{n}\n{p[i]*100:.2f}% / {m[i]:.3f}',xy=(p[i]*100,m[i]),
                xytext=(9,-12),textcoords='offset points',fontsize=8)
ax.plot([p[0]*100,p[1]*100],[m[0],m[1]],color=INK,lw=1.4,ls='--',zorder=2)
ax.annotate('style is bigger but market is dearer:\nthe two rankings disagree',
            xy=((p[0]+p[1])*50,(m[0]+m[1])/2),xytext=(21,0.30),fontsize=8,color=INK,
            arrowprops=dict(arrowstyle='->',color=INK,lw=.9))
ax.set_xlabel('share of total variance (%)');ax.set_ylabel('marginal contribution to risk')
ax.set_xlim(0,66);ax.set_ylim(0.22,0.85)
ax.set_title('Bubble size is the group volatility',loc='left')
