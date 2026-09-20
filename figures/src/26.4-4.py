v=np.array([40_000.,70_000.,50_000.,120_000.])
C=np.array([[1,.25,.45,0],[.25,1,-.15,0],[.45,-.15,1,0],[0,0,0,1]])
sr=np.array([0.0,0.8,0.0,1.6]);d=np.sqrt(251)
def sharpe(k):
    vs=v*np.array([k,1,1,1])
    return (sr/d*vs).sum()/np.sqrt((np.outer(vs,vs)*C).sum())*d
k=np.linspace(0,2,300)
y=[sharpe(t) for t in k]
ax.plot(k,y,color=ACCENT,lw=2.4)
ax.plot(1,sharpe(1),'o',color=INK,ms=8)
ax.plot(0,sharpe(0),'o',color=GOOD,ms=8)
ax.annotate(f'today: {sharpe(1):.4f}',xy=(1,sharpe(1)),xytext=(12,-16),textcoords='offset points',fontsize=8.5)
ax.annotate(f'market hedged away: {sharpe(0):.4f}',xy=(0,sharpe(0)),xytext=(14,4),
            textcoords='offset points',fontsize=8.5,color=GOOD)
s=-0.4858
ax.plot(k,sharpe(1)+s*(k-1)*v[0]/1e5,color=BAD,ls='--',lw=1.5,label='slope from the formula: -0.486 per 100k')
ax.set_xlabel('size multiplier on the market group');ax.set_ylabel('Sharpe Ratio of the book, per year')
ax.set_ylim(1.15,2.15)
ax.set_title('The derivative is right locally; the curve bends away from it',loc='left')
ax.legend(fontsize=7,loc='lower left')
